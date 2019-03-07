import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.tests


with open('test.csv', 'r') as csvfile:
    for line in csvfile:
        FlowArray = []
        sp = line.split(',')
        for i in range(7):
            if sp[i+1] is not None:
            FlowArray.append(sp[i+1])

        collection.insert_one(
        {
        "id": sp[0],
        "Flow" : FlowArray,
        "gender" : sp[8] ,
        "TimeStamp" : sp[9]}
        )
