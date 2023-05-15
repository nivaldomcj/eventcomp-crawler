import logging

import scrapy

from metaevents.spiders.resurchify.constants import BASE_URL
from metaevents.spiders.resurchify.itemloaders import ResurchifyEventItemLoader
from metaevents.spiders.resurchify.items import ResurchifyEventItem
from metaevents.spiders.resurchify.selectors import *
from metaevents.spiders.resurchify.utils import (parse_field_title,
                                                 parse_field_value)


class ResurchifySpider(scrapy.Spider):
    name = 'resurchify'

    # Keep track of which categories we've crawled to avoid go on them again
    seen_category_urls = set()

    # Avoids going through an event twice and also take easy on their servers
    seen_event_ids = set()

    def start_requests(self):
        category_url = BASE_URL.format('computer-science', 1)
        self.seen_category_urls.add(category_url)
        yield scrapy.Request(url=category_url, 
                             callback=self.parse_category)

    def parse_category(self, response):
        def get_category_name(url):
            try:
                return url.split('/')[5]
            except:
                return '*UNKNOWN*'

        for selector in response.css(EVENTS_LIST_ROWS_SELECTOR):
            event_url = selector.css(EVENT_DETAILS_URL_SELECTOR).get()
            if event_url is None:
                continue

            event_id = int(event_url.split('/')[-1])
            if event_id in self.seen_event_ids:
                logging.info('👀 {} (already seen)'.format(event_id))
                continue

            event_category_urls = \
                selector.css(EVENT_DETAILS_CATEGORIES_SELECTOR).getall()
            for category_url in event_category_urls:
                if category_url not in self.seen_category_urls:
                    self.seen_category_urls.add(category_url)
                    logging.info(
                        '🐢 {} (enqueued)'.format(get_category_name(category_url)))
                    yield scrapy.Request(url=category_url,
                                         callback=self.parse_category)

            self.seen_event_ids.add(event_id)
            logging.info('🔍 {} (fetching details...)'.format(event_id))
            yield response.follow(url=event_url, callback=self.parse_event)

        next_page = response.css(EVENT_LIST_NEXT_PAGE_SELECTOR).get()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse_category)
        else:
            logging.info('🏁 {}'.format(get_category_name(response.url)))

    def parse_event(self, response):
        event = ResurchifyEventItemLoader(ResurchifyEventItem(), response)
        event.add_value('id', int(response.url.split('/')[-1]))

        event.add_css('title', EVENT_TITLE_SELECTOR)
        event.add_css('start_at', EVENT_DATE_SELECTOR)
        event.add_css('finish_at', EVENT_DATE_SELECTOR)
        event.add_css('location', EVENT_LOCATION_SELECTOR)
        event.add_css('website', EVENT_WEBSITE_SELECTOR)
        event.add_xpath('categories', EVENT_CATEGORIES_SELECTOR)
        event.add_xpath('description', EVENT_DESCRIPTION_SELECTOR)

        # Fields that may or may not appear in event details depending of event
        metadata = {}
        for selector in response.css(EVENT_METADATA_SELECTOR):
            field_title = parse_field_title(selector.css('th > b::text').get())
            if field_title is not None or field_title != 'event_date':
                field_value = parse_field_value(selector.css('td::text').get())
                metadata[field_title] = field_value
        event.add_value('metadata', metadata)

        yield event.load_item()
