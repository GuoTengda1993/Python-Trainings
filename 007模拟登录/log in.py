# -*- coding: utf-8 -*-
import requests
import http.cookiejar as cookielib


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie未加载')


def login(user, pwd):
    global headers
    url = 'http://218.97.241.83/web/manage.php'
    post_data = {'inputEmail3': user, 'inputPassword3': pwd}
    login_page = session.post(url=url, headers=headers, data=post_data)
    session.cookies.save()
    print(login_page.status_code)
    print('登录成功')


url1 = 'http://218.97.241.83/web/manage.php?act=login'
get_response = requests.get(url=url1, headers=headers)

if '用户登录' in get_response.text:
    login('lansing', '123456')
else:
    print('已经登录')
