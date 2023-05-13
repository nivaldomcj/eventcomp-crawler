import scrapy

from metaevents.spiders.qualis.constants import QUALIS_PERIODICOS_MAIN_PAGE_URL
from metaevents.spiders.qualis.selectors import (
    CLASSIFICATION_RESULT_LINKS_SELECTOR,
    EVENT_CLASSIFICATION_OPTIONS_SELECTOR, RESULT_LINK_ONCLICK_ARGS_SELECTOR)
from metaevents.spiders.qualis.utils import \
    get_request_file_parameters_from_onclick


class QualisSucupiraSpider(scrapy.Spider):
    name = 'qualis-sucupira'

    def start_requests(self):
        yield scrapy.Request(url=QUALIS_PERIODICOS_MAIN_PAGE_URL,
                             callback=self.request_latest_event_classifications)

    def request_latest_event_classifications(self, response):
        # Event Classification is the journal classification from Qualis
        # We are interested in the latest available from platform
        latest_event_classifications_id = \
            response.css(EVENT_CLASSIFICATION_OPTIONS_SELECTOR).getall()
        latest_event_classifications_id = \
            str(max(map(int, latest_event_classifications_id)))
        assert latest_event_classifications_id is not None

        yield scrapy.FormRequest.from_response(
            response,
            formname='form',
            formdata={
                'form:evento': latest_event_classifications_id,
            },
            callback=self.extract_latest_event_classifications
        )

    def extract_latest_event_classifications(self, response):
        for file_link in response.css(CLASSIFICATION_RESULT_LINKS_SELECTOR):
            file_params = get_request_file_parameters_from_onclick(
                file_link.css(RESULT_LINK_ONCLICK_ARGS_SELECTOR).get()
            )
            if file_params is not None:
                yield scrapy.FormRequest.from_response(
                    response,
                    formname='form',
                    formdata=file_params,
                    callback=self.parse_event_classification_spreadsheet,
                )
