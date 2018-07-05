# -*- coding: utf-8 -*-
import scrapy, json
from jsonpath import jsonpath
from scrapy_spider_project.items import *
from datetime import datetime


class ZjfyZhixingCompanySpider(scrapy.Spider):
    name = 'zjfy_zhixing_company'
    allowed_domains = ['www.zjsfgkw.cn']
    start_url = 'http://www.zjsfgkw.cn/Execute/CreditCompany'
    PageNo = 1
    PageSize = 200
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
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
            item = ZjfyCompanyItem()

            item['case_num'] = data['AH']

            item['address'] = data['Address']

            item['publish_time'] = data['BGRQ']

            item['card_id'] = data['CredentialsNumber']

            item['case_time'] = data['LARQ']

            item['company'] = data['ReallyName']

            item['court'] = data['ZXFY']

            item['basis'] = data['ZXYJ']

            item['total_money'] = data['ZXJE']

            item['case_reason'] = data['ZXAY']

            item['debt'] = data['WZXJE']

            item['spider_time'] = datetime.now()

            yield item

        if self.PageNo <= pages:
            self.PageNo += 1

            yield scrapy.FormRequest(url=self.start_url,
                                     formdata={'PageNo': str(self.PageNo),
                                               'PageSize': str(self.PageSize),
                                               'ZXFY': '全部'
                                               }, headers=self.headers, callback=self.parse)



