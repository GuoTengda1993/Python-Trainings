# -*- coding: utf-8 -*-
import xlrd
import xml.dom.minidom as md


def get_xls_data(file_name):
    data = xlrd.open_workbook(file_name)
    table = data.sheet_by_index(0)
    city_list = {}
    for i in range(table.nrows):
        city_list[str(i + 1)] = table.row_values(i)[1]
    return city_list


def write_to_xml(content):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    cities = xmlfile.createElement('cities')
    xmlfile.appendChild(root)
    root.appendChild(cities)
    comment = xmlfile.createComment('城市信息')
    cities.appendChild(comment)

    xmlcotent = xmlfile.createTextNode(str(content))
    cities.appendChild(xmlcotent)

    with open('ciies.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    write_to_xml(get_xls_data('cities.xls'))