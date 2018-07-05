# -*- coding: utf-8 -*-
import scrapy, json
from scrapy_spider_project.items import TianyanItem
from jsonpath import jsonpath


class RegulationsSpider(scrapy.Spider):
    name = 'regulations'
    allowed_domains = ['www.tianyancha.com']
    start_url = 'https://www.tianyancha.com/regulations'

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "aliyungf_tc=AQAAAJNDuDWBOQAAnhSHPUl0OnFNKAot; csrfToken=eRpEYG9E1-JIerbOgbbWnbY2; TYCID=896a4650747111e8ae2d8992bdb6837d; undefined=896a4650747111e8ae2d8992bdb6837d; ssuid=376039019; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1529489165,1529544240,1529544251; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYxOTkxOTU0MSIsImlhdCI6MTUyOTU0NDI3MiwiZXhwIjoxNTQ1MDk2MjcyfQ.URXaksMlIeO7jA-9twfQ_HRfPBkx88DYPyOZGkz5RyoAKCZbs5CJzntKYtRk_yB0YxDkR2uZNPF6TBil4go-dw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252216619919541%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYxOTkxOTU0MSIsImlhdCI6MTUyOTU0NDI3MiwiZXhwIjoxNTQ1MDk2MjcyfQ.URXaksMlIeO7jA-9twfQ_HRfPBkx88DYPyOZGkz5RyoAKCZbs5CJzntKYtRk_yB0YxDkR2uZNPF6TBil4go-dw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1529544365",
        "Host": "www.tianyancha.com",
        "Referer": "https://www.tianyancha.com/regulations",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }

    def start_requests(self):

        yield scrapy.Request(self.start_url, headers=self.headers, callback=self.parse)

    def parse(self, response):

        index_list = [3 * i + 1 for i in range(0, 15)]
        for index in index_list:
            item = TianyanItem()

            node = response.xpath('//tbody/tr[' + str(index) + ']')

            item['type'] = node.xpath('./td[1]/span/text()').extract_first()

            item['title'] = node.xpath('./td[2]/a/text()').extract_first()

            item['org'] = node.xpath('./td[3]/text()').extract_first()

            item['publish_time'] = node.xpath('./td[4]/text()').extract_first()

            item['link'] = node.xpath('./td[2]/a/@href').extract_first()

            yield scrapy.Request(item['link'], meta={"item": item}, headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "aliyungf_tc=AQAAAJNDuDWBOQAAnhSHPUl0OnFNKAot; csrfToken=eRpEYG9E1-JIerbOgbbWnbY2; TYCID=896a4650747111e8ae2d8992bdb6837d; undefined=896a4650747111e8ae2d8992bdb6837d; ssuid=376039019; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1529489165,1529544240,1529544251; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYxOTkxOTU0MSIsImlhdCI6MTUyOTU0NDI3MiwiZXhwIjoxNTQ1MDk2MjcyfQ.URXaksMlIeO7jA-9twfQ_HRfPBkx88DYPyOZGkz5RyoAKCZbs5CJzntKYtRk_yB0YxDkR2uZNPF6TBil4go-dw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252216619919541%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYxOTkxOTU0MSIsImlhdCI6MTUyOTU0NDI3MiwiZXhwIjoxNTQ1MDk2MjcyfQ.URXaksMlIeO7jA-9twfQ_HRfPBkx88DYPyOZGkz5RyoAKCZbs5CJzntKYtRk_yB0YxDkR2uZNPF6TBil4go-dw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1529544489",
                "Host": "www.tianyancha.com",
                "Referer": "https://www.tianyancha.com/regulations/p4",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            }, callback=self.parse_content)

    def parse_content(self, response):
        item = response.meta['item']
        content = response.xpath('//script[@id="_notice_data"]/text()').extract_first()
        jsonobj = json.loads(content)
        item['content'] = jsonpath(jsonobj, '$..PageContent')[0].replace('&nbsp', '').replace('<br/>\n', '').replace('\u3000', '').replace(';', '')
        yield item

