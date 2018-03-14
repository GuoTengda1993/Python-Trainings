import requests
import time
import random
import csv
from bs4 import BeautifulSoup


title_list = ['名字', '价格', '每平米价格', '间数', '面积', '层号', '年份', '经纪人', '地址']
with open('hengshui.csv', 'a+', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(title_list)

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for i in range(1, 51):
    print('现在爬取的是第%d页的数据' % i)
    link = 'https://hengshui.anjuke.com/sale/p' + str(i)
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_='list-item')
    for house in house_list:
        detail_list = []
        name = house.find('div', class_='house-title').a.text.strip()
        price = house.find('span', class_='price-det').text.strip()
        price_square = house.find('span', class_='unit-price').text.strip()
        no_room = house.find('div', class_='details-item').span.text
        area = house.find('div', class_='details-item').contents[3].text
        floor = house.find('div', class_='details-item').contents[5].text
        year = house.find('div', class_='details-item').contents[7].text
        broker = house.find('span', class_='brokername').text
        broker = broker[1:]
        address = house.find('span', class_='comm-address').text.strip()
        address = address.replace('\xa0\xa0\n   ','')
        tag_list = house.find_all('span', class_='item-tags tag-metro')
        tags = [i.text for i in tag_list]
        detail_list = [name, price, price_square, no_room, area, floor, year, broker, address]
        with open('hengshui.csv', 'a+', encoding='utf-8', newline='') as csvfile:
            wrt = csv.writer(csvfile)
            wrt.writerow(detail_list)
        print(name, price, price_square, no_room, area, floor, year, broker, address, tags)
    time.sleep(4+random.random())
