import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.persons


with open('개인.csv', 'r') as csvfile:
    for line in csvfile:
        PersonArray = []
        sp = line.split(',')
        for i in range(19):
            if sp[i] is not "":
            	PersonArray.append(sp[i])

        collection.insert_one(
            {
            "Person" : PersonArray,
            "gender" : sp[19] ,
            "TimeStamp" : sp[20]
            }
        )
