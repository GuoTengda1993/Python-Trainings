# -*- coding: utf-8 -*-
import hmac
import random
import MySQLdb


def hmac_md5(key, pwd):
    return hmac.new(key.encode('utf-8'), pwd.encode('utf-8'), 'MD5').hexdigest()


class User(object):

    with open(r'C:\Users\pc\Desktop\Temp\pwd.txt', 'r') as f:
        pwd = f.readline()
    db = MySQLdb.connect(host='localhost', user='root', password=pwd, db='user_password', charset='utf8')
    cur = db.cursor()

    def __init__(self, name, pwd):
        self.name = name
        self.key = ''.join([chr(random.randint(97, 122)) for i in range(10)])
        self.pwd0 = pwd
        self.pwd = hmac_md5(self.key, pwd)

    def register(self):
        sql = "INSERT INTO userinfo(username, userkey, userpwd) VALUES ('%s', '%s', '%s')" % (self.name, self.key, self.pwd)
        try:
            self.cur.execute(sql)
            self.cur.close()
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def login(self):
        sql = "SELECT userpwd, userkey FROM userinfo WHERE username='{0}'".format(self.name)
        try:
            self.cur.execute(sql)
            values = self.cur.fetchall()
            pwd1 = hmac_md5(values[0][1], self.pwd0)
            if pwd1 == values[0][0]:
                print('登录成功')
        except:
            print('新用户正在注册')
            self.register()


if __name__ == '__main__':
    user1 = User('a', '123456')
    user1.login()
