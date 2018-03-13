# -*- coding: utf-8 -*-
from selenium import webdriver
import os


url = 'https://news.baidu.com/news?fr=mohome&ssid=0&from=844b&uid=&pu=sz%401320_2001%2Cta%40iphone_1_10.3_3_603&bd_page_type=1#/detail/12896848575392312266'
driver = webdriver.PhantomJS()
driver.get(url=url)
content_list = driver.find_elements_by_css_selector('p')
content = ''
for each in content_list:
    content = content + str(each.text)

num1 = content.count('习近平')
print('文章中”习近平“替换的数目为：%s' % num1)
text = content.replace('习近平', '*')
num2 = text.count('一年')
text1 = text.replace('一年', '*')
print('文章中”一年“替换的数目为：%s' % num2)

with open('text.txt', 'w') as f:
    print(text1, file=f)
    f.close()

driver.close()
driver.quit()
