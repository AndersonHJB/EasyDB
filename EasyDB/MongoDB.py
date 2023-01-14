# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 11:21
# @Author  : AI悦创
# @FileName: MongoDB.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import pymongo


class Mongodb(object):
    def __init__(self, database, _set, host="localhost", port=27017):
        self.client = pymongo.MongoClient(host=host, port=port)
        # self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        # self.db = self.client.database
        self.db = self.client[database]
        self.collection = self.db[_set]

    def insert(self, data: dict):
        result = self.collection.insert_one(data)
        return result

    def inserts(self, datas: list):
        result = self.collection.insert_many(datas)
        return result

    def query(self, query: dict):
        result = self.collection.find_one(query)
        return result

    def find_all(self, find_dict):
        result = self.collection.find(find_dict)
        return result

    def update(self, data: dict, key, value):
        query_result = self.query(data)
        query_result[key] = value
        result = self.collection.update(data, query_result)
        return result

    def delete_one(self, data: dict):
        result = self.collection.delete_one(data)
        print(f"本次删除了：{result.deleted_count}")
        return result

    def delete_many(self, data: dict):
        result = self.collection.delete_many(data)
        print(f"本次删除了：{result.deleted_count}")
        return result


if __name__ == '__main__':
    mongodb = Mongodb("hhhhhhhh", "table")
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    student2 = {
        'id': '20170202',
        'name': 'Mike',
        'age': 21,
        'gender': 'male'
    }
    r = mongodb.inserts([student1, student2])
    # r1 = mongodb.delete_many(student1)
    print(r)
    # print(r1)
