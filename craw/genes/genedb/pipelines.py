# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from genedb import settings


class GenedbPipeline(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=settings.DATABASE,
            user=settings.USER,
            password=settings.PASSWORD,
            host=settings.HOST,
            port=settings.PORT)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        names = []
        values = []
        for i in item:
            if item[i]:
                names.append(i)
                if isinstance(item[i], list):
                    values.append("[%s]" % ",".join([str(e) for e in item[i]]))
                else:
                    values.append(str(item[i]))
        try:
            sql = "INSERT INTO genenames(%s) VALUES('%s')" % (",".join(names), "','".join(values))
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.commit()
            with open('db_error.log', 'a+') as file:
                file.write(str(e))

        return item

    def close_spider(self, spider):
        self.conn.close()
