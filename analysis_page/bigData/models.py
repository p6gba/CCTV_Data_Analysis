from django.db import models
from pymongo import MongoClient
import pprint
from bson.son import SON
import datetime


# Create your models here.

class Mongo:
    client = MongoClient('127.0.0.1', 27017);
    database = client.TestDB
    collection = database.dbs

    # 몽고DB CONNECTION
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017);
        self.database = self.client.TestDB
        self.collection = self.database.dbs

    # 몽고DB에서 find
    def GetMongo(self):
        database = self.client.TestDB
        collection = database.dbs
        docs = collection.find({}, {"_id": 0})
        # 딕셔너리 형태로 반환
        {'link': '김우주'}
        return docs

    # 몽고DB에 저장
    def InsertMongo(self):
        database = self.client.TestDB
        collection = database.dbs
        title_id = collection.insert_one({"link": "김우주"})

    # 회원가입 - id 중복 확인
    def Find_id_Mongo(self, key):
        database = self.client.TestDB
        collection = database.dbs
        verfify_id = collection.find({'id': key}, {"_id": 0}).count()
        # 1 or 0으로 반환
        return verfify_id

    # 회원가입 - id, pw, name, email 저장
    def Insert_info_Mongo(self, key1, key2, key3, key4):
        database = self.client.TestDB
        collection = database.dbs
        collection.insert_one({"id": key1, "pw": key2, "name": key3, "email": key4})

    # 로그인 - id가 존재하는지 확인
    def Verify_id_Mongo(self, key):
        database = self.client.TestDB
        collection = database.dbs
        verfify_id = collection.find({'id': key}, {"_id": 0}).count()
        # 1 or 0으로 반환
        return verfify_id

    # 로그인 - id와 pw 둘다 일치하는지 확인
    def Verify_id_pw_Mongo(self, key1, key2):
        database = self.client.TestDB
        collection = database.dbs
        verfify_id_pw = collection.find({'id': key1, 'pw': key2}).count()
        # 1 or 0으로 반환
        return verfify_id_pw

    # HeatMap Json 가져오기
    def Find_HeatMap_Mongo(self):
        database = self.client.test
        collection = database.tests2
        pipline = [
            {"$project": {"Hour": {"$hour": "$TimeStamp"}
                , "Category": "$category name"
                , "_id": 0
                          },
             },
            {
                "$sort": {"Hour": 1, "Category": 1}
            },
            {
                "$group":
                    {
                        "_id": {"Hour": "$Hour", "Category": "$Category"},
                        "count": {"$sum": 1}
                    }

            },
            {
                "$project":
                    {
                        "x": "$_id.Hour",
                        "y": "$_id.Category",
                        "value": "$count",
                        "_id": 0
                    }
            },
            {
                "$sort": {"x": 1}
            }
        ]

        HeatMapData = collection.aggregate(pipline)
        return HeatMapData

    # HeatMap Json Time 가져오기
    def Find_HeatMap_Time_Mongo(self, key1, key2, RadioValue):
        database = self.client.test
        collection = database.tests2
        from_date = key1.split('-')
        to_date = key2.split('-')
        if RadioValue == "all":
            pipline = [
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}},
                {
                    "$project":
                        {
                            "Hour": {"$hour": "$TimeStamp"},
                            "Category": "$category name",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"Hour": 1, "Category": 1}
                },
                {
                    "$group":
                        {
                            "_id": {"Hour": "$Hour", "Category": "$Category"},
                            "count": {"$sum": 1}
                        }
                },
                {
                    "$project":
                        {
                            "x": "$_id.Hour",
                            "y": "$_id.Category",
                            "value": "$count",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"x": 1}
                }
            ]
            HeatMapTimeData = collection.aggregate(pipline)
            return HeatMapTimeData

        elif RadioValue == "man":
            pipline = [
                {
                    "$match":
                        {
                            "gender":
                                {
                                    "$regex": "^1"
                                }
                        }
                }
                ,
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}
                },
                {
                    "$project":
                        {
                            "Hour": {"$hour": "$TimeStamp"},
                            "Category": "$category name",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"Hour": 1, "Category": 1}
                },
                {
                    "$group":
                        {
                            "_id": {"Hour": "$Hour", "Category": "$Category"},
                            "count": {"$sum": 1}
                        }
                },
                {
                    "$project":
                        {
                            "x": "$_id.Hour",
                            "y": "$_id.Category",
                            "value": "$count",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"x": 1}
                }
            ]
            HeatMapTimeData = collection.aggregate(pipline)
            return HeatMapTimeData

        elif RadioValue == "women":
            pipline = [
                {
                    "$match":
                        {
                            "gender":
                                {
                                    "$regex": "^0"
                                }
                        }
                }
                ,
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}
                },
                {
                    "$project":
                        {
                            "Hour": {"$hour": "$TimeStamp"},
                            "Category": "$category name",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"Hour": 1, "Category": 1}
                },
                {
                    "$group":
                        {
                            "_id": {"Hour": "$Hour", "Category": "$Category"},
                            "count": {"$sum": 1}
                        }
                },
                {
                    "$project":
                        {
                            "x": "$_id.Hour",
                            "y": "$_id.Category",
                            "value": "$count",
                            "_id": 0
                        }
                },
                {
                    "$sort": {"x": 1}
                }
            ]
            HeatMapTimeData = collection.aggregate(pipline)
            return HeatMapTimeData

    # 동선 데이터 가져오기
    def Find_Flow_Mongo(self):
        database = self.client.test
        collection = database.flows
        pipline = [
            {
                "$project":
                    {
                        "_id": 0, "Flow": 1
                    }
            }
        ]

        FlowData = collection.aggregate(pipline)
        FlowDataList = []
        for line in FlowData:
            FlowDataList.append((list(line.values())))

        FlowDataRealList = []

        for i in FlowDataList:
            FlowDataRealList.append(i[0])

        return FlowDataRealList

    def Find_Flow_Time_Mongo(self, key1, key2, RadioValue):
        database = self.client.test
        collection = database.flows
        from_date = key1.split('-')
        to_date = key2.split('-')
        if RadioValue == "all":
            pipline = [
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}
                },
                {
                    "$project":
                        {
                            "_id": 0, "Flow": 1
                        }
                }
            ]
            FlowTime = collection.aggregate(pipline)
            FlowTimeList = []
            for line in FlowTime:
                FlowTimeList.append((list(line.values())))

            FlowDataTimeList = []

            for i in FlowTimeList:
                FlowDataTimeList.append(i[0])

            return FlowDataTimeList

        elif RadioValue == "man":
            pipline = [
                {
                    "$match":
                        {
                            "gender":
                                {
                                    "$regex": "^1"
                                }
                        }
                },
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}
                },
                {
                    "$project":
                        {
                            "_id": 0, "Flow": 1
                        }
                }
            ]
            FlowTime = collection.aggregate(pipline)
            FlowTimeList = []
            for line in FlowTime:
                FlowTimeList.append((list(line.values())))

            FlowDataTimeList = []

            for i in FlowTimeList:
                FlowDataTimeList.append(i[0])

            return FlowDataTimeList

        elif RadioValue == "women":
            pipline = [
                {
                    "$match":
                        {
                            "gender":
                                {
                                    "$regex": "^0"
                                }
                        }
                },
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,
                {
                    "$sort": {"TimeStamp": 1}
                },
                {
                    "$project":
                        {
                            "_id": 0, "Flow": 1
                        }
                }
            ]
            FlowTime = collection.aggregate(pipline)
            FlowTimeList = []
            for line in FlowTime:
                FlowTimeList.append((list(line.values())))

            FlowDataTimeList = []

            for i in FlowTimeList:
                FlowDataTimeList.append(i[0])

            return FlowDataTimeList


class MongoProduct:
    client = MongoClient('127.0.0.1', 27017);
    database = client.test
    collection = database.product

    def Find_Product_Mongo(self):
        pipelines = [
            {
                '$group': {'_id': {'Product': '$Product'}, 'total_touch': {'$sum': '$Touch'},
                           'total_buying': {'$sum': '$Buy'}}
            },
            {
                "$sort": {"total_touch": -1}
            },
            {
                "$limit": 10
            }
            ,
            {
                '$project': {'Product': '$_id.Product', 'total_touch': 1, 'total_buying': 1}
            }
            ,
            {
                '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
            }
        ]
        results = self.collection.aggregate(pipelines)
        return results

    def Find_Product_Time_Mongo(self, key1, key2, RadioValue):
        from_date = key1.split('-')
        to_date = key2.split('-')
        if RadioValue == "all":
            pipelines = [
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,

                {
                    "$sort": {"TimeStamp": 1}

                },

                {
                    '$group': {'_id': {'Product': '$Product'}, 'total_touch': {'$sum': '$Touch'},
                               'total_buying': {'$sum': '$Buy'}}
                },
                {
                    "$sort": {"total_touch": -1}
                },
                {
                    "$limit": 10
                }
                ,
                {
                    '$project': {'Product': '$_id.Product', 'total_touch': 1, 'total_buying': 1}
                }
                ,
                {
                    '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
                }
            ]
            results = self.collection.aggregate(pipelines)
            return results


        elif RadioValue == "man":
            pipelines = [
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,

                {
                    "$sort": {"TimeStamp": 1}

                },
                {
                    '$match': {'Gender': '1\n'}
                },
                {
                    '$group': {'_id': {'Product': '$Product'}, 'total_touch': {'$sum': '$Touch'},
                               'total_buying': {'$sum': '$Buy'}}
                },
                {
                    "$sort": {"total_touch": -1}
                },
                {
                    "$limit": 10
                }
                ,
                {
                    '$project': {'Product': '$_id.Product', 'total_touch': 1, 'total_buying': 1}
                }
                ,
                {
                    '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
                }
            ]
            results = self.collection.aggregate(pipelines)
            return results

        elif RadioValue == "women":
            pipelines = [
                {
                    "$match":
                        {
                            "TimeStamp":
                                {
                                    "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                              int(from_date[3]), int(from_date[4]), 0),
                                    "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                              int(to_date[3]), int(to_date[4]), 0)
                                }
                        }
                }
                ,

                {
                    "$sort": {"TimeStamp": 1}

                },
                {
                    '$match': {'Gender': '0\n'}
                },
                {
                    '$group': {'_id': {'Product': '$Product'}, 'total_touch': {'$sum': '$Touch'},
                               'total_buying': {'$sum': '$Buy'}}
                },
                {
                    "$sort": {"total_touch": -1}
                },
                {
                    "$limit": 10
                }
                ,
                {
                    '$project': {'Product': '$_id.Product', 'total_touch': 1, 'total_buying': 1}
                }
                ,
                {
                    '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
                }
            ]
            results = self.collection.aggregate(pipelines)
            return results


class MongoAll:
    client = MongoClient('127.0.0.1', 27017);
    database = client.test
    collection = database.product
    key = ""

    # 몽고DB CONNECTION
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017);
        self.database = self.client.test
        self.collection = self.database.product

    def find_all(self):
        pipelines = [
            {
                '$group': {'_id': {'Product': '$Product'}, 'total_touch': {'$sum': '$Touch'},
                           'total_buying': {'$sum': '$Buy'}}
            },
            {
                "$sort": {"total_touch": -1}
            },
            {
                "$limit": 10
            }
            ,
            {
                '$project': {'Product': '$_id.Product', 'total_touch': 1, 'total_buying': 1}
            }
            ,
            {
                '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
            }
        ]
        results = self.collection.aggregate(pipelines)
        return results

    def find_gender(self, key):
        pipelines = [
            db.cols.aggregate(
                {
                    '$match': {'Gender': key}
                },
                {
                    '$group': {'_id': {'Product': '$Product', 'Gender': '$Gender'}, 'total_touch': {'$sum': '$Touch'},
                               'total_buying': {'$sum': '$Buy'}}
                },
                {
                    "$sort": {"total_touch": -1}
                },
                {
                    "$limit": 10
                }
                ,
                {
                    '$project': {'Product': '$_id.Product', 'Gender': '$_id.Gender', 'total_touch': 1,
                                 'total_buying': 1}
                }
                , {
                    '$project': {'Product': 1, 'total_touch': 1, 'total_buying': 1}
                }
            )

        ]
        results = self.collection.aggregate(pipelines)
        return results

    def find_date(self, key1, key2):
        # pipelines = list()
        # pipelines.append({"$group": {"_id": "$Product", "total_touch": {"$sum": "$Touch"}, "total_buying": {"$sum": "$Buy"}}})
        # pipelines.append({"$match": {"Time": {"$gte": key1, "$lte": key2}}})
        # pipelines.append({"$sort": {"total_touch": -1}})
        # pipelines.append({"$limit": 10})
        pipelines = [
            {
                '$group': {'_id': '$Product', 'total_touch': {'$sum': '$Touch'}, 'total_buying': {'$sum': '$Buy'}}
            },
            {
                "$match": {
                    "Time": {
                        "$gte": key1, "$lte": key2
                    }
                }
            },
            {
                "$sort": {"total_touch": -1}
            },
            {
                "$limit": 10
            }
        ]

        results = self.collection.aggregate(pipelines)
        return results

    def find_date2(self, key1, key2):
        database = self.client.test
        collection = database.flows
        from_date = key1.split('-')
        to_date = key2.split('-')
        pipline = [
            {
                "$match":
                    {
                        "Time":
                            {
                                "$gte": datetime.datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]),
                                                          int(from_date[3]), int(from_date[4]), 0),
                                "$lte": datetime.datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]),
                                                          int(to_date[3]), int(to_date[4]), 0)
                            }
                    }
            }
            ,
            {
                "$sort": {"Time": 1}
            },
            {
                "$group": {"_id": "$Product", "total_touch": {"$sum": "$Touch"}, "total_buying": {"$sum": "$Buy"}}
            }
        ]

        FlowTime = collection.aggregate(pipline)
        FlowTimeList = []
        for line in FlowTime:
            FlowTimeList.append((list(line.values())))

        FlowDataTimeList = []

        for i in FlowTimeList:
            FlowDataTimeList.append(i[0])

        return FlowDataTimeList
