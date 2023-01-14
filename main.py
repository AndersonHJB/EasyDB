# -*- coding: utf-8 -*-
# @Time    : 2023/1/14 14:16
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from EasyDB import Mongodb
from EasyDB import SqliteOperation

if __name__ == '__main__':
    mongodb = Mongodb("kskskskks", "table")
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

    s = SqliteOperation(db_name="test.db", table_name="wswsww")
    print(s.query())
