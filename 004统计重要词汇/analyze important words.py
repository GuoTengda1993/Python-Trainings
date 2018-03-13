# -*- coding: utf-8 -*-
import re
import os
from collections import Counter


dir = r'C:\Users\pc\Desktop\Python Training\004统计重要词汇'
files = os.listdir(dir)
file_list = []
for each in files:
    if re.match('\w+?.txt', each):
        file_list.append(each)
    else:
        pass

useless_list = ['a', 'an', 'the', 'of', 'he', 'she', 'you', 'us', 'they', 'our', 'his', 'her', 'your', 'their', 'is',
                'are', 'if', 'while', 'when', 'where', 'what', 'which', 'and', 'to', 'it', 'i', 'we']
for item in file_list:
    with open(item) as f:
        data = str(f.readlines())
        data = data.lower()
        data = data.replace(r'\n', '')
        words_list = re.split('\W+', data)
        words_list.pop()
    new_list = []
    for word in words_list:
        if word not in useless_list:
            new_list.append(word)
        else:
            pass
    num = Counter(new_list)
    most = num.most_common(1)
    print('In %s the most common word is %s, and the num is %s.' % (item, most[0][0], most[0][1]))
