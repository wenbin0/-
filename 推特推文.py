from selenium import webdriver
from selenium.webdriver import ActionChains
from lxml import etree
import time
from selenium.webdriver.common.keys import Keys
from lxml.html import tostring
from bs4 import BeautifulSoup

browser=webdriver.Chrome()

url='https://twitter.com/search?q=(%23standwithukraine)%20lang%3Aen%20until%3A2022-03-24%20since%3A2022-03-23&src=typed_query'
resp=browser.get(url=url)

''''deng=browser.find_element_by_xpath('//a[@data-testid="loginButton" and @role="link"]')
ActionChains(browser).click(deng).perform()
time.sleep(6)
browser.find_element_by_xpath('//input[@autocomplete="username"]').send_keys('xwb1714739504@gmail.com')
next=browser.find_element_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')
ActionChains(browser).click(next).perform()
time.sleep(1)
password=browser.find_element_by_xpath('//input[@autocomplete="current-password" and @name="password"]').send_keys('xwb20000518ss')
time.sleep(1)
login=browser.find_element_by_xpath('//div[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
time.sleep(1)
ActionChains(browser).click(login).perform()

cookie={'name':'Cookie','value':'guest_id=v1%3A165345324828983263; ct0=b2a35f3643bf5a18e083d6d99e1c98913a7d909c6a566f4f3da647ae2a4729132ecc714b8fc72672f24673876fd2eac2dc663e31ec8527350e3dd56ddbb381aa4f2d8c22054656e9435b0b3644b9cfd9; gt=1529319883678310400; g_state={"i_l":0}; kdt=FmUlEGrJvZOVAEdv1qsjzMqlnbDmdqQiwvIEBhxK; twid=u%3D1381020806545817600; auth_token=6b71833b4ddeb2541d0d995bf07119ab3468fda8; att=1-IjGlWjbWPsIyv8907zjiuhldulxkz8lOID5tmvbK; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A165345324828983263; guest_id_marketing=v1%3A165345324828983263; personalization_id="v1_dDcrfEtA9g1DuoRqKe9Wzw=="; _ga=GA1.2.649576380.1653454200; _gid=GA1.2.482742651.1653454200; lang=en'}
browser.add_cookie(cookie_dict=cookie)
browser.get(url=ur)'''

time.sleep(10)

'''parser=etree.HTML(browser.page_source)
text=parser.xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
ele=text[0].xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]/@id')
ele2=text[1].xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]/@id')
text2=parser.xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]//text()[2]')
text3=parser.xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]//text()[3]')
text4=parser.xpath('//div[@lang="en" and @class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]//text()[4]')'''

text=[]
for k in range(90):
    for j in range(5):
        ActionChains(browser).send_keys(Keys.SPACE).perform()
        time.sleep(1)
    time.sleep(2)
    bs=BeautifulSoup(browser.page_source,'lxml')
    div=bs.find_all('div',{'class':'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'})
    print(len(div),type(div))
    for i in div:
        if i not in text:
            text.append(i)
            print(type(i))
    print(k)
print('-------------------')
print(text,len(text))

for i in text:
    with open('#standwithukraine 2022-03-24.txt', 'a', encoding='utf-8') as f:
        f.write(i.text)
        f.write('\n\n')
        f.write('-----------------------------------------------------------')
        f.write('\n\n')


#browser.quit()

