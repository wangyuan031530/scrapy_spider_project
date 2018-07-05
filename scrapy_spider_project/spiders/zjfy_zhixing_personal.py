# -*- coding: utf-8 -*-
import scrapy, json
from scrapy_spider_project.items import *
from jsonpath import jsonpath
from datetime import datetime

class ZjfyZhixingSpider(scrapy.Spider):
    name = 'zjfy_zhixing_personal'
    allowed_domains = ['www.zjsfgkw.cn']
    start_url = 'http://www.zjsfgkw.cn/Execute/CreditPersonal'
    PageNo = 1
    PageSize = 1000
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "98",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.zjsfgkw.cn",
        "Origin": "http://www.zjsfgkw.cn",
        "Referer": "http://www.zjsfgkw.cn/Execute/CreditPersonal",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    def start_requests(self):

        form_data = {'PageNo': '1', 'PageSize': str(self.PageSize), 'ZXFY': '全部'}

        yield scrapy.FormRequest(self.start_url, formdata=form_data, headers=self.headers, callback=self.parse)

    def parse(self, response):

        jsonobj = json.loads(response.text)

        data_list = jsonpath(jsonobj, '$..informationmodels')[0]

        total = int(jsonpath(jsonobj, '$..total')[0])

        if total % self.PageSize == 0:

            pages = total // self.PageSize

        else:

            pages = total // self.PageSize + 1

        for data in data_list:
            item = ZjfyPersonalItem()

            item['name'] = data['ReallyName']

            item['id_type'] = ''

            item['card_id'] = data['CredentialsNumber']

            item['info_type'] = ''

            item['case_num'] = data['AH']

            item['doc_num'] = ''

            item['publish_org'] = data['ZXFY']

            item['publish_time'] = data['BGRQ']

            item['spider_time'] = datetime.now()

            item['detail_link'] = ''

            item['address'] = ''

            item['case_reason'] = data['ZXAY']

            item['basis'] = data['ZXYJ']

            item['total_money'] = data['ZXJE']

            item['debt'] = data['WZXJE']

            item['court'] = data['ZXFY']

            item['case_time'] = data['LARQ']

            yield item

        if self.PageNo <= pages:
            self.PageNo += 1

            yield scrapy.FormRequest(url=self.start_url,
                                     formdata={'PageNo': str(self.PageNo),
                                               'PageSize': str(self.PageSize),
                                               'ZXFY': '全部'
                                               }, headers=self.headers, callback=self.parse)

