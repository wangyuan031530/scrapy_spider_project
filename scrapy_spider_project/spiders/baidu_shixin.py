# -*- coding: utf-8 -*-
import scrapy, json, pymysql
from jsonpath import jsonpath
from scrapy_spider_project.items import BaiDuShiXinItem
from datetime import datetime


class BaiduShixinSpider(scrapy.Spider):
    name = 'baidu_shixin'
    allowed_domains = ['https://sp0.baidu.com']
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人名单&pn='

    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Host": "sp0.baidu.com",
            "Referer": "https://www.baidu.com/s?ie=UTF-8&wd=失信",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }
    def start_requests(self):
        start_urls = [self.url + str(i * 10) for i in range(10, 30)]
        for start_url in start_urls:
            yield scrapy.Request(start_url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        jsonobj = json.loads(response.text)

        item = BaiDuShiXinItem()

        result = jsonpath(jsonobj, '$..result')

        if result is not False:

            data_list = result[0]

            for data in data_list:

                item['name'] = data['iname']

                item['businessEntity'] = data['businessEntity']

                item['age'] = data['age']

                try:
                    item['sex'] = data['sexy']
                except:
                    item['sex'] = ''

                item['area'] = data['areaName']

                item['card_id'] = data['cardNum']

                item['court'] = data['courtName']

                item['case_num'] = data['caseCode']

                item['gist_id'] = data['gistId']

                item['case_time'] = data['regDate']

                item['gist_unit'] = data['gistUnit']

                item['duty'] = data['duty']

                item['performance'] = data['performance']

                item['disrupt_type'] = data['disruptTypeName']

                item['publish_time'] = data['publishDate']

                item['site_link'] = data['sitelink']

                item['data_id'] = data['loc']

                item['spider_time'] = datetime.now()

                yield item

