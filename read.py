# 2022年3月28日 读取《蜇雷》
from pyquery import PyQuery as pq
import os

base_url = 'http://www.biqugse.com/82167/'
category = pq(url=base_url)
with open(os.getcwd() + '\蜇雷.txt', 'w') as f:
    for i in range(9, len(category('#list dd'))):
        # print(category('#list dd').eq(i).text(), '--', base_url[:-7] + category('#list dd').eq(i)('a').attr('href'))
        doc_url = base_url[:-7] + category('#list dd').eq(i)('a').attr('href')
        doc = pq(url=doc_url)
        print(category('#list dd').eq(i).text())
        f.writelines('\n' + category('#list dd').eq(i).text() + '\n')
        f.writelines(doc('#content').text() + '\n\n')

