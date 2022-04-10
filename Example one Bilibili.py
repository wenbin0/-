from selenium import webdriver
from lxml import etree
import csv
import xlwt

url='https://www.bilibili.com/v/popular/rank/all'
browser=webdriver.Chrome()
response=browser.get(url=url)
page_source=browser.page_source
browser.close()

parse_source=etree.HTML(page_source)
num=parse_source.xpath('//i[contains(@class,"num")]/@class')
num=list(num)
name=parse_source.xpath('//div[@class="info"]/a/text()')
watch=parse_source.xpath('//span[@class="data-box"][1]/text()')
watch=[i.strip() for i in watch]
author=parse_source.xpath('//span[contains(@class,"up-name")]/text()')
author=[i.strip() for i in author]
barrage=parse_source.xpath('//span[@class="data-box"][2]/text()')
barrage=[i.strip() for i in barrage]

#for i in author:
#    print(i)

'''with open('Example one Bilibili.csv','w',encoding='utf-8') as file:
    write=csv.writer(file)
    write.writerow(['排名','标题','观看量','作者','弹幕量'])
    for i in num,name,watch,author,barrage:
        write.writerow(i)'''

workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('Example one',cell_overwrite_ok=True)
list=['排名','标题','观看量','作者','弹幕量']
for i in range(5):
    worksheet.write(0,i,list[i])
for i in range(1,101):
    worksheet.write(i,0,num[i-1])
for j in range(1,101):
    worksheet.write(j,2,watch[j-1])
for j in range(1,101):
    worksheet.write(j,1,name[j-1])
for j in range(1,101):
    worksheet.write(j,3,author[j-1])
for j in range(1,101):
    worksheet.write(j,4,barrage[j-1])

workbook.save('Bilibili.xls')









