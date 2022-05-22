from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
import xlwt
import time
browser=webdriver.Chrome()
url='https://www.ashleyfurniture.com/c/furniture/living-room/sofas/'
responser=browser.get(url=url)
time.sleep(20)
'''#users=browser.find_element_by_xpath('//a[@class="user-account"]')
#ActionChains(browser).click(users).perform()
#red=browser.find_element_by_xpath('//a[@class="redesign-button"]')
#ActionChains(browser).click(red).perform()
browser.find_element_by_xpath('//input[@class="input-text email required" and @type="email"]').send_keys('xwb1714739504@gmail.com')
browser.find_element_by_xpath('//input[@class="input-text  required" and @name="dwfrm_login_password"]').send_keys('nQX8BRMmX8fr59N!')
browser.find_element_by_xpath('//input[@class="form-row form-row-button btn-wrapper" and @type="submit"]').click()

start=browser.find_element_by_xpath('//div[@class="start-shopping"]')
ActionChains(browser).click(start).perform()
'''
browser.find_element_by_xpath('//input[@type="email"]').send_keys('xwb1714739504@gmail.com')
browser.find_element_by_xpath('//input[@type="text" and @class="offer-control input input-field"]').send_keys('17147')
browser.find_element_by_xpath('//div[@id="Submit1-Item22"]').click()
browser.find_element_by_xpath('//button[@class="offer-control close " and @role="button"]').click()

page_source=browser.page_source
parser=etree.HTML(page_source)
def link():
    xlink=parser.xpath('//a[@class="thumb-link"]/@href')
    next_page=browser.find_element_by_xpath('//div[@class="search-result-options search-result-options-bottom"]//span')
    '''for i in range(16):
        #next_page.click()
        ActionChains(browser).click(next_page).perform()
        parser1=etree.HTML(browser.page_source)
        add=parser1.xpath('//a[@class="thumb-link"]/@href')
        for j in add:
            xlink.append(j)'''
    return xlink

for i in link():
    resp = browser.get(i)
    pa = etree.HTML(browser.page_source)
    click = browser.find_element_by_xpath('//button[@class="country-us-btn"]')
    ActionChains(browser).click(click).perform()
    name = pa.xpath('//div[@class="product-name"]/h1/text()')
    lian = i
    width = pa.xpath('//div[@class="detail-row detail-row-dimensions"]//li')[0]
    depth = pa.xpath('//div[@class="detail-row detail-row-dimensions"]//li')[1]
    height = pa.xpath('//div[@class="detail-row detail-row-dimensions"]//li')[2]
    weight = pa.xpath('//div[@class="detail-row"]/h3[text()="weight"]//../text()')
    seat_height = pa.xpath('//div[@class="detail-row"]/ul/li')[1]
    seat_depth = pa.xpath('//div[@class="detail-row"]/ul/li')[0]
    # leg_height=pa.xpath('//div[@class="detail-row"]/ul/li')[6]
    arms = pa.xpath('//div[@class="detail-row"]/ul/li')[2]
    fabric = pa.xpath('//div[@class="detail-row"]/h3[text()="Fabric Details"]//..//li/text()')
    print(name)
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('sofas',cell_overwrite_ok=True)
list=['商品名称','商品链接','重量','材质','width','depth','height','座深','座高','扶手间距离']
for i in range(9):
    worksheet.write(0,i,list[i])
for i in range(259):
    worksheet.write(i+1,0,name)
for i in range(259):
    worksheet.write(i+1,1,lian)
for i in range(259):
    worksheet.write(i+1,2,weight)
for i in range(259):
    worksheet.write(i+1,3,fabric)
for i in range(259):
    worksheet.write(i+1,4,width)
for i in range(259):
    worksheet.write(i+1,5,depth)
for i in range(259):
    worksheet.write(i+1,6,height)
for i in range(259):
    worksheet.write(i+1,7,seat_height)
for i in range(259):
    worksheet.write(i+1,8,seat_depth)
for i in range(259):
    worksheet.write(i+1,9,arms)
workbook.save('sofa.xls')
#print(page_source)



browser.quit()
