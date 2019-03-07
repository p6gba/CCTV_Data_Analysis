import csv
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.product
collection = db.cols4


with open('cols3.csv', 'r') as csvfile:
    for line in csvfile:
        sp = line.split(',')
        d = datetime.datetime.strptime(sp[6], "%Y-%m-%d %H:%M \n").strftime('%Y-%m-%dT%H:%M:00.000Z')
	
        collection.insert_one({"ID": sp[0], "Customer" : sp[1], "Product" : sp[2] , "Touch" : int(sp[3]), "Buy":int(sp[4]), "Gender":sp[5], "Time":d})
