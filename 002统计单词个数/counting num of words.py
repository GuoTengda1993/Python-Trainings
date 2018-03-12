# -*- coding:utf-8 -*-
import re


article = ''
with open('test.txt') as f:
    article = f.read().strip()
format_article = re.split('\W+', article)
format_article.pop()
# print(format_article)
print(len(format_article))
