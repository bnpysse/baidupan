# 2022年3月28日 读取《蜇雷》
from pyquery import PyQuery as pq

base_url = 'http://www.biqugse.com/82167/'
doc = pq(url=base_url)

for i in range(9, len(doc('#list dd'))):
    print(doc('#list dd').eq(i).text(), '--', base_url[:-7] + doc('#list dd').eq(i)('a').attr('href'))


