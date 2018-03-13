# -*- coding: utf-8 -*-
import xlwt


def write_xls(list):
    workbook = xlwt.Workbook(encoding='utf-8')
    data_sheet = workbook.add_sheet('cities')
    for i in range(len(list)):
        for x in range(len(list[i])):
            data_sheet.write(i, x, list[i][x])
    workbook.save('cities.xls')


with open('city.txt') as f:
    cities = f.readlines()
n = 0
city_list = []
for each in cities:
    if ':' in each:
        item = each.strip()
        item = item.replace(',', '')
        item = item.replace('"', '')
        city = item.split(':')
        city_list.append(city)
        n += 1
    else:
        pass

write_xls(city_list)
