import logging

import scrapy

from metaevents.spiders.wikicfp.constants import BASE_URL
from metaevents.spiders.wikicfp.itemloaders import WikiCfpEventItemLoader
from metaevents.spiders.wikicfp.items import WikiCfpEventItem
from metaevents.spiders.wikicfp.selectors import *
from metaevents.spiders.wikicfp.utils import (get_category_name,
                                              get_event_dates, get_event_id,
                                              select_field_value)
from metaevents.utils import parse_field_title, parse_field_value


class WikiCfpSpider(scrapy.Spider):
    name = 'wikicfp'

    # Keep track of which categories we've crawled to avoid go on them again
    seen_category_names = set()

    # Also due to an strange bug on their pagination, keep track of urls too
    seen_page_urls = set()

    # Avoids going through an event twice and also take easy on their servers
    seen_event_ids = set()

    # Which category will we grab first?
    first_category_name = 'computer science'

    def start_requests(self):
        category_url = BASE_URL.format(self.first_category_name)
        self.seen_category_names.add(self.first_category_name)
        yield scrapy.Request(url=category_url, callback=self.parse_category)

    def parse_category(self, response):
        if response.url not in self.seen_page_urls:
            self.seen_page_urls.add(response.url)

        category_name = get_category_name(response.url)

        for event_url in response.css(CATEGORY_EVENT_URLS_SELECTOR).getall():
            event_id = get_event_id(event_url)

            if event_id in self.seen_event_ids:
                logging.info('👀 {} (already seen)'.format(event_id))
                continue
            
            logging.info('🔍 {} (fetching details...)'.format(event_id))
            self.seen_event_ids.add(event_id)
            yield response.follow(
                url=event_url,
                callback=self.parse_event,
                cb_kwargs={'event_id': event_id,
                           'event_main_category': category_name, },
            )

        next_page = response.css(CATEGORY_NEXT_PAGE_SELECTOR).get()
        if next_page is not None:
            next_url = response.urljoin(next_page)
            if next_url not in self.seen_page_urls:
                self.seen_page_urls.add(next_url)
                yield response.follow(next_url, callback=self.parse_category)
            else:
                logging.info('🏁 {} (skipping, seen)'.format(response.url))
        else:
            logging.info('🏁 {} (done)'.format(category_name))

    def parse_event(self, response, event_id, event_main_category):
        event = WikiCfpEventItemLoader(WikiCfpEventItem(), response)
        event.add_value('id', event_id)
        event.add_css('title', EVENT_TITLE_SELECTOR)
        event.add_css('type', EVENT_TYPE_SELECTOR)
        event.add_css('start_at', EVENT_START_AT_SELECTOR)
        event.add_css('finish_at', EVENT_FINISH_AT_SELECTOR)
        event.add_css('location', EVENT_LOCATION_SELECTOR)
        event.add_css('website', EVENT_WEBSITE_SELECTOR)
        event.add_css('description', EVENT_DESCRIPTION_SELECTOR)

        event_categories = set([event_main_category, ])
        for selector in response.css(EVENT_CATEGORIES_SELECTOR):
            category_name = selector.css('::text').get()
            category_url = selector.css('::attr("href")').get()
            event_categories.add(category_name)

            if category_name not in self.seen_category_names:
                self.seen_category_names.add(category_name)
                logging.info('🐢 {} (enqueued)'.format(category_name))
                yield response.follow(category_url, callback=self.parse_category)
        event.add_value('categories', list(event_categories))

        event_metadata = dict()
        for selector in response.css(EVENT_METADATA_SELECTOR):
            field_title = parse_field_title(selector.css('th::text').get())
            if field_title is None or field_title in ('when', 'where'):
                continue

            field_value = parse_field_value(select_field_value(selector))
            if field_value is not None:
                event_metadata[field_title] = field_value
        event.add_value('metadata', event_metadata)

        yield event.load_item()
