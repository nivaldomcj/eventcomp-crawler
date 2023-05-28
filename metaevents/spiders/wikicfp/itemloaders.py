from dateparser import parse
from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from metaevents.functions import html_to_text


class WikiCfpEventItemLoader(ItemLoader):
    id_out = TakeFirst()

    title_out = TakeFirst()

    type_out = TakeFirst()

    start_at_in = MapCompose(lambda x: parse(x) if isinstance(x, str) else None)
    start_at_out = TakeFirst()

    finish_at_in = MapCompose(lambda x: parse(x) if isinstance(x, str) else None)
    finish_at_out = TakeFirst()

    location_out = TakeFirst()

    website_out = TakeFirst()

    description_in = TakeFirst()
    description_out = Compose(html_to_text)

    metadata_out = TakeFirst()