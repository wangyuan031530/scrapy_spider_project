# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiDuShiXinItem(scrapy.Item):
    # 被执行自然人/组织单位
    name = scrapy.Field()
    # 法人
    businessEntity = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # 省份
    area = scrapy.Field()
    # 身份证号码/组织机构代码
    card_id = scrapy.Field()
    # 执行法院
    court = scrapy.Field()
    # 案号
    case_num = scrapy.Field()
    # 执行依据文号
    gist_id = scrapy.Field()
    # 立案时间
    case_time = scrapy.Field()
    # 做出执行依据单位
    gist_unit = scrapy.Field()
    # 生效法律文书确定的义务
    duty = scrapy.Field()
    # 被执行人的履行情况
    performance = scrapy.Field()
    # 失信被执行人行为具体情形
    disrupt_type = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 源网址链接
    site_link = scrapy.Field()
    # 数据id
    data_id = scrapy.Field()
    # 爬取时间
    spider_time = scrapy.Field()


class BjsatItem(scrapy.Item):
    #数据唯一ID
    data_id = scrapy.Field()
    #发布单位
    publish_org = scrapy.Field()
    #发布时间
    publish_time = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 纳税人类型
    taxpayer_type = scrapy.Field()
    # 纳税人识别号
    identity_num = scrapy.Field()
    # 负责人姓名
    name = scrapy.Field()
    # 证件号码
    card_id = scrapy.Field()
    # 经营地点
    address = scrapy.Field()
    # 欠税税种
    tax_type = scrapy.Field()
    # 欠税余额
    tax_amount = scrapy.Field()
    # 当前新发生的欠税余额
    new_tax_amount = scrapy.Field()
    # 爬取时间
    spider_time = scrapy.Field()


class ZjfyPersonalItem(scrapy.Item):
    #姓名
    name = scrapy.Field()
    #证件号码
    card_id = scrapy.Field()
    #地址
    address = scrapy.Field()
    #案号
    case_num = scrapy.Field()
    #案由
    case_reason = scrapy.Field()
    #执行依据
    basis = scrapy.Field()
    #标的金额
    total_money = scrapy.Field()
    #未执行金额
    debt = scrapy.Field()
    #执行法院
    court = scrapy.Field()
    #发布单位
    publish_org = scrapy.Field()
    #发布时间
    publish_time = scrapy.Field()
    #立案时间
    case_time = scrapy.Field()
    #爬取时间
    spider_time = scrapy.Field()
    #证件类型
    id_type = scrapy.Field()
    #信息类型
    info_type = scrapy.Field()
    #执行依据文号
    doc_num = scrapy.Field()
    #详情链接
    detail_link = scrapy.Field()


class ZjfyCompanyItem(scrapy.Item):
    #案号
    case_num = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 证件号码
    card_id = scrapy.Field()
    # 立案时间
    case_time = scrapy.Field()
    #公司或组织名称
    company = scrapy.Field()
    # 未执行金额
    debt = scrapy.Field()
    # 案由
    case_reason = scrapy.Field()
    # 执行法院
    court = scrapy.Field()
    # 标的金额
    total_money = scrapy.Field()
    # 执行依据
    basis = scrapy.Field()
    #爬取时间
    spider_time = scrapy.Field()

class TianyanItem(scrapy.Item):

    type = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    org = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()


class JudicialItem(scrapy.Item):
    cAjBh = scrapy.Field()
    lm = scrapy.Field()
    dtUpdatetime = scrapy.Field()
    qzpx = scrapy.Field()
    cBh = scrapy.Field()
    cah = scrapy.Field()
    cygMc = scrapy.Field()
    czsfgXm = scrapy.Field()
    sf = scrapy.Field()
    czw = scrapy.Field()
    cayBh = scrapy.Field()
    cajlb = scrapy.Field()
    cggnr = scrapy.Field()
    ssSf = scrapy.Field()
    cnr = scrapy.Field()
    cslfy = scrapy.Field()
    cbh = scrapy.Field()
    dtFbsj = scrapy.Field()
    cgglx = scrapy.Field()
    cslfyMc = scrapy.Field()
    ssxq = scrapy.Field()
    cfymc = scrapy.Field()
    dtKtrq = scrapy.Field()
    cbt = scrapy.Field()
    cggbt = scrapy.Field()
    najlb = scrapy.Field()
    esFymc = scrapy.Field()
    tnr = scrapy.Field()
    ccbftBh = scrapy.Field()
    cbgMc = scrapy.Field()
    spider_time = scrapy.Field()

class HeBeiZhixingItem(scrapy.Item):
    #诉讼地位
    status = scrapy.Field()
    #被执行人姓名/名称
    name = scrapy.Field()
    #被执行人类型
    executor_type = scrapy.Field()
    #证件类型
    id_type = scrapy.Field()
    #证件号码
    card_id = scrapy.Field()
    #被执行人性别
    sex = scrapy.Field()
    #被执行人年龄
    age = scrapy.Field()
    #案号
    case_num = scrapy.Field()
    #立案日期
    case_time = scrapy.Field()
    #执行法院
    court = scrapy.Field()
    #案件状态
    case_status = scrapy.Field()
    #申请执行标的金额
    total_money = scrapy.Field()
    #执行依据文书编号
    doc_num = scrapy.Field()
    #经办机构（做出执行依据单位）
    gist_unit = scrapy.Field()
    #发布日期
    publish_time = scrapy.Field()
    #详情链接
    detail_link = scrapy.Field()
    #爬取时间
    spider_time = scrapy.Field()







