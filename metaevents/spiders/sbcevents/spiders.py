from datetime import datetime

import scrapy

from metaevents.spiders.sbcevents.constants import BASE_URL
from metaevents.spiders.sbcevents.selectors import (
    CALENDAR_EVENT_URL_SELECTOR, CALENDAR_NEXT_PAGE_SELECTOR)


class SbcEventsSpider(scrapy.Spider):
    name = 'sbcevents'

    def start_requests(self):
        current_year = datetime.now().year
        for year in range(current_year, current_year + 5):
            yield scrapy.Request(
                url=BASE_URL.format(year),
                callback=self.parse_calendar
            )

    def parse_calendar(self, response):
        for event_url in response.css(CALENDAR_EVENT_URL_SELECTOR).getall():
            yield response.follow(
                url=event_url,
                callback=self.parse_event
            )

        next_page = response.css(CALENDAR_NEXT_PAGE_SELECTOR).get()
        if next_page is not None:
            yield response.follow(
                url=next_page,
                callback=self.parse_calendar
            )

    def parse_event(self, response):
        event_title = response.css('div.jev_evdt_title::text').getall()
        if not event_title:
            event_title = response.css('title::text').getall()

        event_summary = response.css('div.jev_evdt_summary::text').getall()
        event_description = response.css('div.jev_evdt_desc').getall()
        event_location = response.css('.jev_evdt_location::text').get()
        return {
            'event_title': event_title,
            'event_summary': event_summary,
            'event_description': event_description,
            'event_location': event_location,
        }
