# -*- coding: utf-8 -*-
import scrapy,time
from scrapy_spider_project.items import HeBeiZhixingItem
from datetime import datetime

class HebeicourtSpider(scrapy.Spider):
    name = 'heBeiCourt'
    allowed_domains = ['http://sswy.hbsfgk.org']

    def start_requests(self):
        start_urls = ['http://hbgy.hbsfgk.org/zxsxPage.jspx?channelId=458&listsize=18195&pagego=' + str(i) for i in range(1, 18196)]
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse, headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "hbgy.hbsfgk.org",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    })

    def parse(self, response):
        item = HeBeiZhixingItem()
        node_list = response.xpath('//*[@class="sswy_news"]/li')

        for node in node_list:

            item['detail_link'] = node.xpath('./a/@href').extract_first()

            yield scrapy.Request(item['detail_link'],callback=self.parse_detail,headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Host": "sswy.hbsfgk.org:7080",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }, meta={'item':item})

            time.sleep(5)

    def parse_detail(self, response):
        item = response.meta['item']

        item['status'] = response.xpath('//*[class="fd_table_02"]/tr[1]/td[2]/text()').extract_first()

        item['name'] = response.xpath('//*[class="fd_table_02"]/tr[2]/td[2]/text()').extract_first()

        item['executor_type'] = response.xpath('//*[class="fd_table_02"]/tr[3]/td[2]/text()').extract_first()

        item['id_type']= response.xpath('//*[class="fd_table_02"]/tr[4]/td[2]/text()').extract_first()

        item['card_id']= response.xpath('//*[class="fd_table_02"]/tr[5]/td[2]/text()').extract_first()

        item['sex']= response.xpath('//*[class="fd_table_02"]/tr[6]/td[2]/text()').extract_first()

        item['age']= response.xpath('//*[class="fd_table_02"]/tr[7]/td[2]/text()').extract_first()

        item['case_num']= response.xpath('//*[class="fd_table_02"]/tr[8]/td[2]/text()').extract_first()

        item['case_time']= response.xpath('//*[class="fd_table_02"]/tr[9]/td[2]/text()').extract_first()

        item['court']= response.xpath('//*[class="fd_table_02"]/tr[10]/td[2]/text()').extract_first()

        item['case_status']= response.xpath('//*[class="fd_table_02"]/tr[11]/td[2]/text()').extract_first()

        item['total_money']= response.xpath('//*[class="fd_table_02"]/tr[12]/td[2]/text()').extract_first()

        item['doc_num']= response.xpath('//*[class="fd_table_02"]/tr[13]/td[2]/text()').extract_first()

        item['gist_unit']= response.xpath('//*[class="fd_table_02"]/tr[14]/td[2]/text()').extract_first()

        item['publish_time']= response.xpath('//*[class="fd_table_02"]/tr[15]/td[2]/text()').extract_first()

        item['spider_time']= datetime.now()

        yield item



