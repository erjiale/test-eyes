from bs4 import *
import requests as rq
import os

r2 = rq.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%83%AD%E7%8B%97&oq=%E7%83%AD%E7%8B%97&rsp=-1")
print(r2.content)

soup2 = BeautifulSoup(r2.text, "html.parser")
print(soup2.prettify())
# links = []

# container = soup2.find_all('img', {'class'='main_img'})
# # # book_container = warning.nextSibling.nextSibling

# # photos = soup2.find_all('img')
# # print(photos[0])
# # myphotos = soup2.select('img[data-imgurl^=""]')

# for img in container:
#     links.append(img['src'])

# for l in links:
#     print(l)