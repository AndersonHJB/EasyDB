# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 09:49
# @Author  : AI悦创
# @FileName: SqliteOperation.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import sqlite3


class SqliteOperation(object):
    def __init__(self, db_name: str, table_name: str):
        """
        link: https://bornforthis.cn/column/pyauto/auto_base10.html
        :param db_name:
        :param table_name:
        """
        self.db = sqlite3.connect(db_name)
        self.table = table_name

    def query(self):
        """查询语句"""
        # 查询语句
        query_sql = f"select * from {self.table}"
        return list(self.db.execute(query_sql))

    def delete(self, key: str, value):
        delete_sql = f"delete from {self.table} where {key}={value}"
        self.db.execute(delete_sql)
        self.db.commit()

    def update(self, update_sql):
        # update_sql = "update aiyc set author = '不匿名' where id >= 4"
        self.db.execute(update_sql)
        self.commit()

    def insert_many(self, insert_data: list):
        # length = len(insert_data)
        # for i in insert_data:
        # insert_sql = f"insert into {self.table}(title, content, author) values ('第{}个标题', '随机的第{}个内容', '匿名')"
        for data_sql in insert_data:
            self.db.execute(data_sql)
            self.db.commit()
