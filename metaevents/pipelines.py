import pymongo
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MongoDbPipeline:

    def __init__(self, mongo_uri, mongo_database):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=str(crawler.settings.get("MONGODB_URI")),
            mongo_database=str(crawler.settings.get("MONGODB_DATABASE")),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.database = self.client[self.mongo_database]
        self.database.drop_collection(spider.name)
        self.collection = self.database[spider.name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class DuplicatesPipeline:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        item_id = adapter["id"] if hasattr(adapter, 'id') else None

        if item_id is not None:
            if item_id in self.ids_seen:
                raise DropItem(f"Duplicate item found: {item!r}")
            else:
                self.ids_seen.add(item_id)

        return item
