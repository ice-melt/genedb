#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : main.py
@Time       : 2019/6/5 上午11:00
@Version    : 1.0  
@Desc       : None
"""

from scrapy import cmdline

cmdline.execute("scrapy crawl hgnc".split())
