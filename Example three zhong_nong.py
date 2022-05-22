from selenium import webdriver
from lxml import etree
#from selenium.webdriver import ActionChains
from lxml.html import tostring
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
#url='http://cbs.cau.edu.cn/col/col31815/index.html'
#browser.get(url=url)

for i in range(26,39):
    urlx='http://cbs.cau.edu.cn/col/col318'+str(i)+'/index.html'
    browser.get(url=urlx)
    parser = etree.HTML(browser.page_source)
    plink = parser.xpath('//ul[@class="upic"]/li/a/@href')


    for j in plink:
        link = 'http://cbs.cau.edu.cn' + j
        browser.get(url=link)
        parser1 = etree.HTML(browser.page_source)
        summary=parser1.xpath('//td[@style="word-break: break-all;"]/text()')
        summary='姓名：'+str(summary).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        #summary=parser1.xpath('//td[@style="-ms-word-break: break-all;"]/text()')
        #summary='简介：'+str(summary).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        imf=parser1.xpath('//p[@style="text-indent: 2em;"]//text()')
        imf='信息：'+str(imf).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        edu_exp=parser1.xpath('//ol[@class=" list-paddingleft-2"]//text()')
        edu_exp='教育经历'+str(edu_exp).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        phone=parser1.xpath('//span[@style="font-family: 宋体; font-size: 16px;"][last()-2]/text()')
        phone='电话：'+str(phone).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        mail=parser1.xpath('//span[@style="font-family: 宋体; font-size: 16px;"][last()-1]/text()')
        mail='邮箱：'+str(mail).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        address=parser1.xpath('//span[@style="font-family: 宋体; font-size: 16px;"][last()]/text()')
        address='地址：'+str(address).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        font=parser1.xpath('//span[contains(@style,"font-family:宋体")]/text()')
        font='其余：'+str(font).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        aa='详情链接：'+link
        result=[summary,imf,edu_exp,phone,mail,address,font,aa]
        with open('biology.txt','a',encoding='utf-8') as file:
            file.write('\n'.join(result))
            file.write('\n'+'='*50+'\n')
    #for j in plink:
    #print(tostring(plink, encoding='utf-8').decode('utf-8'))


browser.quit()
#print(tostring(parser1,encoding='utf-8').decode('utf-8'))

