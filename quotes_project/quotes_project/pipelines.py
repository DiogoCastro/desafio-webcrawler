from pymongo import MongoClient
from itemadapter import ItemAdapter


class QuotesProjectPipeline:
    collection_name = 'diogo_castro'

    def __init__(self, mongo_uri, mongo_db):
        # self.conn = MongoClient('localhost', 27017)
        # db = self.conn['quotestoscrape']
        # self.collection = db['diogo_castro']
        self.mongo_uri = mongo_uri
        self.mongo_db = 'quotestoscrape'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # self.collection.insert(dict(item))
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
