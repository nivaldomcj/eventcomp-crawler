from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from metaevents.functions import html_to_text
from metaevents.spiders.resurchify.functions import parse_resurchify_date


class ResurchifyEventItemLoader(ItemLoader):
    id_out = TakeFirst()

    categories_in = MapCompose(lambda x: x.strip())
    categories_out = MapCompose(lambda x: x.lower())

    description_in = TakeFirst()
    description_out = Compose(html_to_text)

    title_out = TakeFirst()

    location_in = MapCompose(lambda x: x.strip())
    location_out = TakeFirst()

    website_out = TakeFirst()

    start_at_in = TakeFirst()
    start_at_out = Compose(lambda v: parse_resurchify_date(v, False))

    finish_at_in = TakeFirst()
    finish_at_out = Compose(lambda v: parse_resurchify_date(v, True))

    metadata_out = TakeFirst()
