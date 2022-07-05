from selenium import webdriver
from selenium.webdriver import ActionChains
from lxml import etree
import time
from selenium.webdriver.common.keys import Keys
import xlwt

browser=webdriver.Chrome()

url='https://www.youtube.com/'
resp=browser.get(url=url)
'''send=browser.find_element_by_xpath('//input[@id="search"]').send_keys('Olympic Flame Lighting Ceremony Tokyo 2020')#.
button=browser.find_element_by_xpath('//button[@id="search-icon-legacy"]')
ActionChains(browser).click(button).perform()
time.sleep(2)
tar=browser.find_element_by_xpath('//a[@href="/watch?v=yD58s2ikdHE"]')#.
ActionChains(browser).click(tar).perform()
time.sleep(3)
ag=browser.find_element_by_xpath('//yt-formatted-string/span[@dir="auto"]')
ActionChains(browser).click(ag).perform()
urlx='https://www.youtube.com/watch?v=yD58s2ikdHE'
name='Olympic Flame Lighting Ceremony Tokyo 2020'
def spi():
    pin=[]
    idx_list=[]
    zan_list=[]
    timex_list=[]
    for k in range(50):#5次100数据
        for j in range(50):
            ActionChains(browser).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.1)
        time.sleep(1)
        par1=etree.HTML(browser.page_source)

        idx=par1.xpath('//span[@class="style-scope ytd-comment-renderer"]//text()')
        for i in idx:
            idx_list.append(i)

        pinlun2 = par1.xpath('//yt-formatted-string[@id="content-text"]/span[1]/text()')
        pinlun1 = par1.xpath('//yt-formatted-string[@id="content-text"]/text()')
        for c in pinlun1:
            pin.append(c)
        for d in pinlun2:
            pin.append(d)

        zan=par1.xpath('//span[@id="vote-count-middle"]//text()')
        for i in zan:
            zan_list.append(i)

        timex=par1.xpath('//yt-formatted-string[@class="published-time-text above-comment style-scope ytd-comment-renderer"]/a[@class="yt-simple-endpoint style-scope yt-formatted-string"]//text()')
        for i in timex:
            timex_list.append(i)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet', cell_overwrite_ok=True)
    list=['视频url','视频标题','评论id','评论内容','赞','时间']
    for i in range(6):
        worksheet.write(0, i, list[i])
    for i in range(len(idx_list)):
        worksheet.write(i + 1, 0, urlx)
    for i in range(len(idx_list)):
        worksheet.write(i + 1, 1, name)
    for i in range(len(idx_list)):
        worksheet.write(i + 1, 2,idx_list[i])
    for i in range(len(pin)):
        worksheet.write(i + 1, 3, pin[i])
    for i in range(len(zan_list)):
        worksheet.write(i + 1, 4,zan_list[i])
    for i in range(len(timex_list)):
        worksheet.write(i + 1, 5,timex_list[i])
    workbook.save('东奥会评论4.xls')
    print(len(pin),len(idx_list))'''


'''    for b in pin:
        with open('.//东京奥运评论7.txt','a',encoding='utf-8') as f:
            f.write(b)
            f.write('\n')
    for e in pi:
        with open('.//东京奥运评论7.txt','a',encoding='utf-8') as f:
            f.write(e)
            f.write('\n\n')
    #for a in s:
    #    print(a)

    #print(browser.page_source)'''
#spi()


#browser.quit()



