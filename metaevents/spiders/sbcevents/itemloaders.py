from itemloaders.processors import Compose, TakeFirst
from scrapy.loader import ItemLoader

from metaevents.functions import html_to_text
from metaevents.spiders.sbcevents.functions import (parse_sbc_event_date,
                                                    parse_sbc_event_title)


class SbcEventItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

    title_in = Compose(parse_sbc_event_title)

    start_at_in = Compose(lambda x: parse_sbc_event_date(x[0]))

    finish_at_in = Compose(lambda x: parse_sbc_event_date(x[1]))

    description_in = Compose(html_to_text)
