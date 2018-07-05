# -*- coding: utf-8 -*-
import scrapy,json
from scrapy_spider_project.items import JudicialItem
from jsonpath import jsonpath
from datetime import datetime


class KtggSpider(scrapy.Spider):
    name = 'ktgg'
    allowed_domains = ['https://splcgk.court.gov.cn']
    pageNum = 1
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length":"20",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "splcgk.court.gov.cn",
        "Origin": "https://splcgk.court.gov.cn",
        "Referer": "https://splcgk.court.gov.cn/gzfwww//ktgg",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    def start_requests(self):
        start_url = 'https://splcgk.court.gov.cn/gzfwww//ktgglist?pageNo=' + str(self.pageNum)

        yield scrapy.FormRequest(start_url, formdata={"pageNum": str(self.pageNum)}, callback=self.parse,headers=self.headers)

    def parse(self, response):

        jsonobj = json.loads(response.text, strict=False)

        node_list = jsonpath(jsonobj, '$..data')[0]

        pages = int(jsonpath(jsonobj, '$..pages')[0])

        for node in node_list:
            item = JudicialItem()

            item['cAjBh'] = node['cAjBh']
            item['lm'] = node['lm']
            item['dtUpdatetime'] = node['dtUpdatetime']
            item['qzpx'] = node['qzpx']
            item['cBh'] = node['cBh']
            item['cah'] = node['cah']
            item['cygMc'] = node['cygMc']
            item['czsfgXm'] = node['czsfgXm']
            item['sf'] = node['sf']
            item['czw'] = node['czw']
            item['cayBh'] = node['cayBh']
            item['cajlb'] = node['cajlb']
            item['cggnr'] = node['cggnr']
            item['ssSf'] = node['ssSf']
            item['cnr'] = node['cnr']
            item['cslfy'] = node['cslfy']
            item['cbh'] = node['cbh']
            item['dtFbsj'] = node['dtFbsj']
            item['cgglx'] = node['cgglx']
            item['cslfyMc'] = node['cslfyMc']
            item['ssxq'] = node['ssxq']
            item['cfymc'] = node['cfymc']
            item['dtKtrq'] = node['dtKtrq']
            item['cbt'] = node['cbt']
            item['cggbt'] = node['cggbt']
            item['najlb'] = node['najlb']
            item['esFymc'] = node['esFymc']
            item['tnr'] = node['tnr']
            item['ccbftBh'] = node['ccbftBh']
            item['cbgMc'] = node['cbgMc']
            item['spider_time'] = datetime.now()

            yield item

        if self.pageNum < pages:

            self.pageNum += 1

            url = 'https://splcgk.court.gov.cn/gzfwww//ktgglist?pageNo=' + str(self.pageNum)

            yield scrapy.FormRequest(url, formdata={"pageNum": str(self.pageNum)}, callback=self.parse, headers=self.headers, dont_filter=True)





