#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : HGNC.py
@Time       : 2019/6/5 上午10:43
@Version    : 1.0  
@Desc       : None
"""
import scrapy
import json
from genedb.items import GeneNameItem


class HGNCSpider(scrapy.Spider):
    name = 'hgnc'
    allowed_domains = ['genenames.org']
    # start_urls = ['http://itcast.cn/']
    start_urls = ("http://rest.genenames.org/fetch/status/Approved",)

    def parse(self, response):
        print("##################ok 进来啦 ==")

        # items = []

        data = json.loads(response.body_as_unicode())
        for doc in data['response']['docs']:
            item = GeneNameItem()
            for k in doc:
                if k == 'mamit-trnadb':
                    item['mamit_trnadb'] = doc[k]
                elif k == '_version_':
                    item['version'] = doc[k]
                elif k == 'pseudogene.org':
                    item['pseudogene_org'] = doc[k]
                else:
                    item[k] = doc[k]
            yield item
