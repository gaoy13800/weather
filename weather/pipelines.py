# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi
class WeatherPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    #采用同步机制写入mysql

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd= settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )

        dbpool = adbapi.ConnectionPool("pymysql", **dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)

        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)



    def do_insert(self, cursor, item):
        #执行具体的插入
        insert_sql, params = item.get_insert_sql()

        cursor.execute(insert_sql, params)