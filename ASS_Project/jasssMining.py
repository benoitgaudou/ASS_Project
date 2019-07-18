#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thursday Jul 4 15:43:00 2019

@author: kevin
"""
from urllib import request

import bs4
import os

from pathlib import Path

from article_scrap import JasssArticle
from article_scrap.JasssScrap import doi_converter

url_JASSS = "http://jasss.soc.surrey.ac.uk/index_by_issue.html"
req_text = request.urlopen(url=url_JASSS).read()

page = bs4.BeautifulSoup(req_text, "lxml")

itr: int = 0

tp = Path(os.getcwd()+"/data/")

for gen in page.findAll("p", {'class': 'item'}):
    itr += 1
    url_article = gen.find("a")['href']
    print(str(itr)+" => "+url_article)
    article = JasssArticle(url=url_article)

    if article.is_review():
        break

    res_file = str(tp)+"/JASSS_" + doi_converter(article.doi()) + ".txt"
    print(res_file)
    os.makedirs(os.path.dirname(res_file), exist_ok=True)

    article.save(res_file)
