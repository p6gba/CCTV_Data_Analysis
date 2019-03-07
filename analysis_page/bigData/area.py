import csv
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.test
collection = db.product


with open('backup_csv_product.csv', 'r') as csvfile:
    for line in csvfile:
        sp = line.split(',')
        d = datetime.datetime.strptime(str(sp[4]), "%Y-%m-%dT%H:%M:%S.000Z")
        collection.insert_one({"id": sp[0], "Product": sp[1], "Touch" : int(sp[2]), "Buy" : int(sp[3]) , "TimeStamp" : d, "Gender" : int(sp[5])})
