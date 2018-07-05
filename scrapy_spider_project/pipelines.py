# -*- coding: utf-8 -*-
import pymysql, scrapy_spider_project.settings, pymongo
from scrapy_spider_project.items import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiDuShiXinPipeline(object):
    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER,
                                    password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, BaiDuShiXinItem):
            insert_sql = 'insert into shixin_info(name, businessEntity, age, sex, area, card_id, court, case_num, gist_id, case_time, gist_unit, duty, performance, disrupt_type, publish_time, site_link, data_id, spider_time) values (%s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            params = [item['name'], item['businessEntity'], item['age'], item['sex'], item['area'],
                      item['card_id'], item['court'], item['case_num'], item['gist_id'],
                      item['case_time'], item['gist_unit'], item['duty'], item['performance'],
                      item['disrupt_type'], item['publish_time'], item['site_link'], item['data_id'],
                      item['spider_time']]
            self.cursor.execute(insert_sql, params)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class BjsatPipeline(object):

    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER,
                                    password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        if isinstance(item, BjsatItem):

            insert_sql = 'insert into taxlist(data_id, ' \
                         'company, identity_num, name, card_id, ' \
                         'publish_org, publish_time, spider_time, ' \
                         'address, taxpayer_type, tax_type, tax_amount, ' \
                         'new_tax_amount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            params = [item['data_id'], item['company'], item['identity_num'], item['name'],
                      item['card_id'], item['publish_org'], item['publish_time'], item['spider_time'],
                      item['address'], item['taxpayer_type'],  item['tax_type'], item['tax_amount'], item['new_tax_amount']]

            self.cursor.execute(insert_sql, params)

            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class ZjfyPersonalPipeline(object):

    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ZjfyPersonalItem):
            insert_sql = 'insert into zhixing_info(name, id_type, card_id, info_type, case_num, doc_num, publish_org, publish_time, spider_time, detail_link, address, case_reason, basis, total_money, debt, court, case_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            params = [item['name'],item['id_type'],item['card_id'],item['info_type'],item['case_num'],item['doc_num'],item['publish_org'],item['publish_time'],item['spider_time'],item['detail_link'],item['address'],item['case_reason'],item['basis'],item['total_money'],item['debt'],item['court'],item['case_time']]
            self.cursor.execute(insert_sql, params)

            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class ZjfyCompanyPipeline(object):
    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER,
                                    password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ZjfyCompanyItem):
            insert_sql = 'insert into company_zhixing_info(case_num, address, publish_time, card_id, case_time, company, debt, case_reason, court, total_money, basis, spider_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            params = [item['case_num'], item['address'],item['publish_time'],item['card_id'],item['case_time'],item['company'],item['debt'],item['case_reason'],item['court'],item['total_money'],item['basis'], item['spider_time']]
            self.cursor.execute(insert_sql, params)
            self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


class TianyanPipeline(object):
    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER,
                                    password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, TianyanItem):
            insert_sql = 'insert into tianyan(type, title, publish_time, org, content, link) values (%s, %s, %s, %s, %s, %s)'
            params = [item['type'], item['title'], item['publish_time'], item['org'], item['content'], item['link']]
            self.cursor.execute(insert_sql, params)
            self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


class KtggPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.db = self.client['ktgg']
        self.sheet = self.db['judicial']

    def process_item(self, item, spider):
        if isinstance(item,JudicialItem):
            self.sheet.insert(dict(item))
        return item


class HebeiZhixingPipeline(object):
    def __init__(self):
        settings = scrapy_spider_project.settings
        self.conn = pymysql.connect(host=settings.MYSQL_HOST, port=3306, user=settings.MYSQL_USER,
                                    password=settings.MYSQL_PASSWORD, db=settings.MYSQL_DBNAME, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item,HeBeiZhixingItem):
            insert_sql = 'insert into test(name, id_type, card_id, case_num, doc_num, publish_time, spider_time, detail_link, total_money, court, case_time, status, executor_type, sex, age, case_status, gist_unit) '
            params = [item['name'],item['id_type'],item['card_id'],item['case_num'],item['doc_num'],item['publish_time'],item['spider_time'], item['detail_link'],item['total_money'],item['court'],item['case_time'],item['status'], item['executor_type'],item['sex'],item['age'],item['case_status'],item['gist_unit']]
            self.cursor.execute(insert_sql,params)
            self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()





