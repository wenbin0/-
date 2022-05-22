import requests
from lxml import etree
from lxml.html import tostring
'''def City():
    city='https://www.lianjia.com/city/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
             }
    response_city=requests.get(url=city,headers=headers)
    parse_city=etree.HTML(response_city.text)
    link_city=parse_city.xpath('//div[@class="city_province"]//li/a/@href')
    name_city=parse_city.xpath('//div[@class="city_province"]//li/a/text()')

    return link_city
    for i in link_city:
        print(i)
    for j in name_city:
        print(j)
#City（）是所有城市的链接

for q in City():
    url=q+'xiaoqu/'  '''
linkx=[]
url='https://wh.lianjia.com/xiaoqu/?from=rec'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
         }
cookies={'cookie':'BAIDUID=0189A07E1101A164C16EAFD24E93926E:FG=1; BIDUPSID=8516D946F1658F32C25FF059C0E457BB; PSTM=1632470890; ab_jid=29c86df71dc5e219ffead3104415bdb01a70; ab_bid=6fa3751d0f79cff9983dc6ed95b1e9cfbaa2; __yjs_duid=1_c25594bdb465db9bf435d4deb43b31771632484680332; BDUSS=Ux3cGRLTXVBdTZ3aFlHQ01JN0w4dzNOTTNUdFl1OXJBMU5IU3NYbmxmVTc1ek5pRUFBQUFBJCQAAAAAAAAAAAEAAABHYqyzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADtaDGI7WgxiT; MCITY=-48%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=2ka1ak852g2h2g058k1h8eoho14; ZFY=YzNlKn:BCbc01ZIzSdJwWLcsNti7F3HmTO:Az4RnsHqbs:C; ab_sr=1.0.1_NGFhYzc4MmNhMzQ1MGNjMTYxNTJkZDdkODFhNGM4NzEwNjkyYzQ5NGE4MTQ5YzA5NTBhYjFmMDA0NTM1NGM4YTEzYWZmNjUwNzIxMjAxNjZhOThkNGQ2ZTYyMjlkYWQxMDkxNDI5YTdkZTQ5NWM0OTVlNzU4YWIxOWE0ZjhkNmViMzBiYmVmOGUyNWI3ZmJjY2RjM2JlMjhlYzljODExOA=='}
resp=requests.get(url=url,headers=headers)
#print(resp.text)
#page=resp.text
par=etree.HTML(resp.text)
#print(tostring(par))
link1=par.xpath('//div[@class="info"]/div[@class="title"]/a/@href')
for l in link1:
    linkx.append(l)

for x in range(2,3):
    url1 = 'https://wh.lianjia.com/xiaoqu/pg{}/?from=rec'.format(x)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
               }
    cookies = {
        'cookie': 'BAIDUID=0189A07E1101A164C16EAFD24E93926E:FG=1; BIDUPSID=8516D946F1658F32C25FF059C0E457BB; PSTM=1632470890; ab_jid=29c86df71dc5e219ffead3104415bdb01a70; ab_bid=6fa3751d0f79cff9983dc6ed95b1e9cfbaa2; __yjs_duid=1_c25594bdb465db9bf435d4deb43b31771632484680332; BDUSS=Ux3cGRLTXVBdTZ3aFlHQ01JN0w4dzNOTTNUdFl1OXJBMU5IU3NYbmxmVTc1ek5pRUFBQUFBJCQAAAAAAAAAAAEAAABHYqyzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADtaDGI7WgxiT; MCITY=-48%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=2ka1ak852g2h2g058k1h8eoho14; ZFY=YzNlKn:BCbc01ZIzSdJwWLcsNti7F3HmTO:Az4RnsHqbs:C; ab_sr=1.0.1_NGFhYzc4MmNhMzQ1MGNjMTYxNTJkZDdkODFhNGM4NzEwNjkyYzQ5NGE4MTQ5YzA5NTBhYjFmMDA0NTM1NGM4YTEzYWZmNjUwNzIxMjAxNjZhOThkNGQ2ZTYyMjlkYWQxMDkxNDI5YTdkZTQ5NWM0OTVlNzU4YWIxOWE0ZjhkNmViMzBiYmVmOGUyNWI3ZmJjY2RjM2JlMjhlYzljODExOA=='}
    resp = requests.get(url=url1, headers=headers)
    # print(resp.text)
    # page=resp.text
    par = etree.HTML(resp.text)
    # print(tostring(par))
    link = par.xpath('//div[@class="info"]/div[@class="title"]/a/@href')
    for p in link:
        if p not in linkx:
            linkx.append(p)

#print(len(linkx))
#for r in linkx:
#    print(r)
na=[]
photo=[]
a=0
#print(na)
for i in linkx:
    resp1=requests.get(url=i,headers=headers)
    par1=etree.HTML(resp1.text)
    result=par1.xpath('//li[@class="img-item"]/@data-src')
    name = par1.xpath('//li[@class="img-item"]/img/@alt')
    for j in result:
        photo.append(j)
    for k in name:
        na.append(k)

for o in photo:
    req=requests.get(o)
    with open('.//链家图//{}.jpg'.format(na[a]),'wb') as f:
        f.write(req.content)
    a+=1



'''for i in link:
    print(i)
'''

