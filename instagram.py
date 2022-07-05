from selenium import webdriver
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import queue
from lxml import etree
from bs4 import BeautifulSoup
import xlwt


browser=webdriver.Chrome()
url='https://www.instagram.com'
resp=browser.get(url=url)

time.sleep(1)
def logi():
    account=browser.find_element_by_xpath('//input[@aria-label="手机号、帐号或邮箱"]').send_keys('xwb1714739504@gmail.com')
    password=browser.find_element_by_xpath('//input[@aria-label="密码"]').send_keys('xwb20000518ss')
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(3)
    yihou=browser.find_element_by_xpath('//button[text()="以后再说"]')
    ActionChains(browser).click(yihou).perform()
    time.sleep(0.5)
    search=browser.find_element_by_xpath('//input[@aria-label="搜索输入"]').send_keys('y_haiku')
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(3)
logi()

links=[]
img_links=[]
for i in range(300):
    for j in range(2):
        perf=ActionChains(browser).send_keys(Keys.SPACE).perform()
        time.sleep(0.5)
    time.sleep(1)
    parser=etree.HTML(browser.page_source)
    href=parser.xpath('//div[@class="v1Nh3 kIKUG _bz0w"]/a/@href')
    img_link=parser.xpath('//div[@class="v1Nh3 kIKUG _bz0w"]//img/@src')
    for o in img_link:
        if o not in img_links:
            img_links.append(o)
    print(len(img_links))
    for o in href:
        link='https://www.instagram.com'+o
        if link not in links:
            links.append(link)
    print('去重后',len(links))


time.sleep(3)
browser.switch_to.new_window('tab')
authors=[]
zans=[]
timexs=[]
lis=[]
for li in links:
    browser.get(url=li)
    time.sleep(1)
    par=BeautifulSoup(browser.page_source,'lxml')

    '''for i in par.find_all('div',{'class':'MOdxS '}):
        authors.append(i.text)
        print(i.text)
    for i in par.find_all('section',{'class':'EDfFK ygqzn '}):
        for x in i.find_all('span'):
            zans.append(x.text)
            print(x.text)
    for i in par.find_all('div',{'class':'NnvRN '}):
        for x in i.find_all('time'):
            timexs.append(x.text)
            print(x.text)'''
    parser1=etree.HTML(browser.page_source)
    author=parser1.xpath('//div[@class="C4VMK"]//span[@class="_7UhW9   xLCgt      MMzan   KV-D4            se6yk       T0kll "]//text()')
    author=str(author).replace('\n','').replace(' ','').replace('\'','')
    authors.append(author)
    zan=parser1.xpath('//section[@class="EDfFK ygqzn "]//span/text()')
    zans.append(zan)
    timex=parser1.xpath('//div[@class="NnvRN "]//time/@title')
    timexs.append(timex)

    lis.append(li)

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet', cell_overwrite_ok=True)
list=['url','作者内容','点赞数','时间','图片链接','评论数']
for i in range(6):
    worksheet.write(0, i, list[i])
for i in range(len(links)):
    worksheet.write(i + 1, 0, links[i])
for i in range(len(authors)):
    worksheet.write(i + 1, 1, authors[i])
for i in range(len(zans)):
    worksheet.write(i + 1, 2,zans[i])
for i in range(len(timexs)):
    worksheet.write(i + 1, 3,timexs[i])
for i in range(len(img_links)):
    worksheet.write(i + 1, 4, img_links[i])
workbook.save('inst.xls')
a=0
for i in img_links:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    req = requests.get(url=i, headers=headers)
    with open('.//ins图片//{}.jpg'.format(a), 'ab') as f:
        f.write(req.content)
    a += 1





'''login=browser.find_element_by_xpath('//button[@type="submit"]')
ActionChains(browser).click(login).perform()
time.sleep(2)'''