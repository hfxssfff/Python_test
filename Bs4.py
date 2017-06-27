import requests,bs4
import io
import sys
import time

print('KITE')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码
#爬取天气网页
begintime = time.time()
res7 = requests.get('https://kite.com/docs/python/threading.Semaphore')
res7.encoding = 'utf-8'
res7.raise_for_status()
Webhtml7 = bs4.BeautifulSoup(res7.text,"html5lib")
print(Webhtml7)
endtime = time.time()
print('运行时间为：'+str(endtime-begintime)+'s')
