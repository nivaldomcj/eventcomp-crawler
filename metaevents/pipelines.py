import pymongo
from itemadapter import ItemAdapter


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

    def __connect(self, collection_name):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.database = self.client[self.mongo_database]
        self.collection = self.database[collection_name]

    def __set_seen_ids(self, spider):
        seen_ids = set()
        for document in self.collection.find({}, {'_id': 0, 'id': 1}):
            seen_ids.add(document['id'])
        if hasattr(spider, 'seen_event_ids'):
            spider.seen_event_ids = seen_ids

    def __continue_crawling(self, spider, _continue):
        if _continue:
            self.__set_seen_ids(spider)
        else:
            self.database.drop_collection(spider.name)

    def open_spider(self, spider):
        self.__connect(spider.name)
        self.__continue_crawling(spider, False)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item
