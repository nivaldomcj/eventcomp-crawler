from dateparser import parse
from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from metaevents.functions import html_to_text


class WikiCfpEventItemLoader(ItemLoader):
    id_out = TakeFirst()

    title_in = TakeFirst()
    title_out = Compose(lambda x: x.strip() if isinstance(x, str) else None)

    type_in = TakeFirst()
    type_out = Compose(lambda x: x.strip() if isinstance(x, str) else None)

    start_at_in = TakeFirst()
    start_at_out = Compose(lambda x: parse(x) if isinstance(x, str) else None)

    finish_at_in = TakeFirst()
    finish_at_out = Compose(lambda x: parse(x) if isinstance(x, str) else None)

    location_out = TakeFirst()

    website_out = TakeFirst()

    description_in = TakeFirst()
    description_out = Compose(html_to_text)

    metadata_out = TakeFirst()