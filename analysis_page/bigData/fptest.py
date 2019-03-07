import pyfpgrowth
from django.db import models
from pymongo import MongoClient
import pprint
from bson.son import SON
import datetime


# Create your models here.

class Mongo:
    client = MongoClient('127.0.0.1', 27017);
    database = client.test
    collection = database.flows2

    # 몽고DB CONNECTION
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017);
        self.database = self.client.test
        self.collection = self.database.flows2

    def Find_fp_Mongo(self):
        database = self.client.test
        collection = database.flows2
        docs = collection.find({},{'Flow':1, '_id' : 0})
        FlowDataList = []
        for line in docs:
            datalist = list(line.values())
            FlowDataList.append(datalist[0])

        return FlowDataList

connection = Mongo()
lis = connection.Find_fp_Mongo()

patterns = pyfpgrowth.find_frequent_patterns(lis, 8000)
rules = pyfpgrowth.generate_association_rules(patterns, 0.2)
print("패턴:", patterns, "\n룰:", rules)
