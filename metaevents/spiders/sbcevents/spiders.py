import scrapy

from metaevents.spiders.sbcevents.constants import BASE_URL


class SbcEventsSpider(scrapy.Spider):
    name = 'sbcevents'

    # Which years from SBC Events Calendar we will fetch
    years = [2023, ]

    def start_requests(self):
        for year in self.years:
            yield scrapy.Request(url=BASE_URL.format(year),
                                 callback=self.parse_calendar)

    def parse_calendar(self, response):
        for event_url in response.css('a.ev_link_row::attr("href")').getall():
            yield response.follow(url=event_url,
                                  callback=self.parse_event)

        next_page_url = response.css('a[title="Próximo"]::attr("href")').get()
        if next_page_url:
            yield response.follow(url=next_page_url,
                                  callback=self.parse_calendar)

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
