from datetime import datetime

import scrapy

from metaevents.spiders.sbcevents.constants import BASE_URL
from metaevents.spiders.sbcevents.itemloaders import SbcEventItemLoader
from metaevents.spiders.sbcevents.items import SbcEventItem
from metaevents.spiders.sbcevents.selectors import *


class SbcEventsSpider(scrapy.Spider):
    name = 'sbcevents'

    def start_requests(self):
        current_year = datetime.now().year
        for year in range(current_year, current_year + 5):
            yield scrapy.Request(url=BASE_URL.format(year),
                                 callback=self.parse_calendar)

    def parse_calendar(self, response):
        event_urls = response.css(CALENDAR_EVENT_URL_SELECTOR).getall()
        for event_url in event_urls:
            yield response.follow(url=event_url, callback=self.parse_event)

        next_page = response.css(CALENDAR_NEXT_PAGE_SELECTOR).get()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse_calendar)

    def parse_event(self, response):
        event = SbcEventItemLoader(SbcEventItem(), response)
        event.add_css('title', EVENT_PAGE_TITLE_SELECTOR)
        event.add_css('title', EVENT_CALENDAR_TITLE_SELECTOR)
        event.add_css('start_at', EVENT_CALENDAR_DATES_SELECTOR)
        event.add_css('finish_at', EVENT_CALENDAR_DATES_SELECTOR)
        event.add_css('description', EVENT_CALENDAR_DESCRIPTION_SELECTOR)
        event.add_css('location', EVENT_CALENDAR_LOCATION_SELECTOR)
        yield event.load_item()
