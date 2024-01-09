# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class CryptoDataPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017) # creates a connection
        db = self.conn['crypto_db'] #database name
        self.collection = db['currency'] # collection name

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item)) # adds item to the database
        return item
