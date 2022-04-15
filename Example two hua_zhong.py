from selenium import webdriver
from lxml import etree
from lxml.html import tostring,fromstring
import xlwt
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
url = 'http://faculty.hust.edu.cn/xklb.jsp?urltype=tree.TreeTempUrl&wbtreeid=1004'
response = browser.get(url=url)
page_source = browser.page_source
parser = etree.HTML(page_source)

'''personal_link=parser.xpath('//li[@class="shezhiyincangjiaoshi"]/a/@href')
for i in personal_link:
    res = browser.get(url=i)
    page = browser.page_source
    parser1=etree.HTML(page)

    name=parser1.xpath('//div[@class="info"]/h2/text()')
    name='姓名：'+str(name).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    imformation=parser1.xpath('//div/p/text()')
    imformation='基本信息：'+str(imformation).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    #imformation = parser1.xpath('//ul[@class="clearfix"]/li/text()')
    edu_exp=parser1.xpath('//div[@class="blockwhite Edu-exp"]//div[@class="cont"]//text()')
    edu_exp='教育经历：'+str(edu_exp).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    res_dic=parser1.xpath('//div[@class="blockwhite Rsh-focus"]//div[@class="cont"]//text()')
    res_dic='研究方向：'+str(res_dic).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    like=parser1.xpath('//span[@id="_parise_obj_u8"]/text()')
    like='人气：'+str(like).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    link='详情链接：'+i
    with open('pyhsics.txt','a',encoding='utf-8') as file:
        file.write('\n'.join([name,imformation,edu_exp,res_dic,like,link]))
        file.write('\n'+'='*50+'\n')'''

def link():
    #click_link=parser.xpath('//h3[@onclick="javascript:querycteacheru6(11623,1)"]')
    click_link=browser.find_element_by_xpath('//h3[@onclick="javascript:querycteacheru6(11623,1)"]')
    click_link.click()
    #imformation=browser.find_element_by_xpath('//h4/text()')
    page_source1=etree.HTML(browser.page_source)
    personal_link=page_source1.xpath('//li[@class="shezhiyincangjiaoshi"]/a/@href')
    next_page=browser.find_elements_by_xpath('//div[@class="pages"]//a[text()="下一页"]/..')[0]
    #print(tostring(next_page,encoding='utf-8').decode('utf-8'))
    for i in range(49):
        #ActionChains(browser).click(next_page).perform()
        next_page.click()
        page_source2=etree.HTML(browser.page_source)
        add=page_source2.xpath('//li[@class="shezhiyincangjiaoshi"]/a/@href')
        for i in add:
            personal_link.append(i)
    return personal_link

for i in link():
    res = browser.get(url=i)
    page = browser.page_source
    parser1=etree.HTML(page)
    name0=parser1.xpath('//div[@class="photo-text fr"]/h3/text()')
    name1=parser1.xpath('//div[@class="info"]/h2[1]/text()')
    name2=parser1.xpath('//p[@class="name"]/span[1]/text()')
    name3=parser1.xpath('//div[@class="t_photo"]/span/text()')
    name4=parser1.xpath('//div[@class="photo fl"]/h2/strong/text()')
    name5=parser1.xpath('//div[@class="name"]/h1/text()')
    name=[name0,name1,name2,name3,name4,name5]

    #name=name[j]
    name='姓名:'+str(name).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
        
    imformation00=parser1.xpath('//div[@class="intro-text"]//text()')
    imformation11=parser1.xpath('//div[@class="cont"]//text()')
    imformation22=parser1.xpath('//div[@class="edu"]//text()')
    imformation33=parser1.xpath('//div[@class="t_jbxx_nr"]//text()')
    imformation44=parser1.xpath('//div[@class="sec-item per-info"]//text()')
    imformation5=parser1.xpath('//div[@class="account"]/p/text()')
    imformation=[imformation00,imformation11,imformation22,imformation33,imformation44,imformation5]

    imformation='基本信息：'+str(imformation).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    #print(imformation,type(imformation))
    edu_exp0=parser1.xpath('//div[@class="tab-con" and @style="display: block;"]//text()')
    edu_exp1=parser1.xpath('//div[@class="blockwhite Edu-exp"]/div[@class="cont"]//text()')
    edu_exp2=parser1.xpath('//div[@class="edu"]//text()')
    edu_exp3=parser1.xpath('//ul[@class="t_edu_nr"]//text()')
    edu_exp4=parser1.xpath('//div[@class="on"]//text()')
    edu_exp5=parser1.xpath('//div[@class="edu"]//text()')
    edu_exp=[edu_exp0,edu_exp1,edu_exp2,edu_exp3,edu_exp4,edu_exp5]
    edu_exp='教育经历：'+str(edu_exp).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    #print(edu_exp)
    
    res_dic0=parser1.xpath('//div[@class="tab-inner"]/text()')
    res_dic1=parser1.xpath('//div[@class="blockwhite Rsh-focus"]//text()')
    res_dic2=parser1.xpath('//i[@style="position: relative;z-index: 999;"]//text()')
    res_dic3=parser1.xpath('//div[@class="bd"]//text()')
    res_dic4=parser1.xpath('//li[@class="direction"]//text()')
    res_dic5=parser1.xpath('//div[@class="research"]//text()')
    res_dic=[res_dic0,res_dic1,res_dic2,res_dic3,res_dic4,res_dic5]

    res_dic='研究方向/职位：'+str(res_dic).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    #print(res_dic)
    like0=parser1.xpath('//span[@id="_parise_obj_u7"]/text()')
    like1=parser1.xpath('//span[@id="_parise_obj_u8"]/text()')
    like2=parser1.xpath('//span[@id="_parise_obj_u6"]/text()')
    like3=parser1.xpath('//span[@id="_parise_obj_u13"]/text()')
    like4=parser1.xpath('//p[@id="_parise_obj_u7"]/text()')
    like=[like0,like1,like2,like3]

    like='人气：'+str(like).replace('\n','').replace(' ','').replace('\xa0','').replace('\\n','').replace('\'','')
    #print(like)
    link_im = '详情链接：' + i
    #print(link_im)
    with open('science.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([name, imformation, edu_exp, res_dic, like, link_im]))
        file.write('\n' + '=' * 50 + '\n')

browser.close()





#for i in personal_link:
#    print(i)

