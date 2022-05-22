from selenium import webdriver
from lxml import etree
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
browser=webdriver.Chrome()
url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B8%A3%D7%D6&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDEsNiw1LDQsNyw4LDIsOQ%3D%3D'
res=browser.get(url=url)
a=1
link=[]
par=etree.HTML(browser.page_source)
lin=par.xpath('//img[@class="main_img img-hover"]/@data-imgurl')
#print(lin)
for k in lin:
    link.append(k)
#print(link)
for i in range(16):
    for j in range(50):
        ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(0.1)

    par1=etree.HTML(browser.page_source)
    lin1=par1.xpath('//img[@class="main_img img-hover"]/@data-imgurl')
    for o in lin1:
        if o not in link:
            link.append(o)
#print(link)
print(len(link))

for x in link:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    req=requests.get(url=x,headers=headers)
    #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'
    with open('.//tupian//{}.jpg'.format(a),'ab') as f:
        f.write(req.content)
    a+=1
browser.quit()
