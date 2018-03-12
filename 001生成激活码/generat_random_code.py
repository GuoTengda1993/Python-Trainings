# -*- coding:utf-8 -*-
import random
import MySQLdb

letter_list = []
for i in range(97, 123):
    lower_letter = str(chr(i))
    letter_list.append(lower_letter)
for i in range(65, 91):
    upper_letter = str(chr(i))
    letter_list.append(upper_letter)
for i in range(10):
    num = str(i)
    letter_list.append(i)


def generate_code(n,m):
    global letter_list
    code_list = []
    for x in range(n):
        code = ''
        for y in range(m):
            letter = str(random.choice(letter_list))
            code = code + letter
        code_list.append(code)
    return code_list


def insert_to_db(list):
    password = str(input('Please input the password of MySQL:'))
    db = MySQLdb.connect(host='localhost', user='root', password=password)
    cursor = db.cursor()
    try:
        cursor.execute('USE random_code')
    except:
        cursor.execute("CREATE DATABASE random_code CHARACTER SET 'utf8'")
        cursor.execute('USE random_code')
        cursor.execute('CREATE TABLE content(codes VARCHAR(256) NOT NULL)')
    try:
        for each_code in list:
            cursor.execute('INSERT INTO content(codes) VALUES ("%s")' % each_code)
        cursor.close()
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ ==  '__main__':
    n = int(input('Please input the num of codes:'))
    m = int(input('Please input the num of letters in each code:'))
    codelist = generate_code(n, m)
    for each in codelist:
        print(each)
    insert_to_db(codelist)