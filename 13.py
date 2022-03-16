'''
q=[1,2,3,4,5]
w=[1,2,3]
def containsAny():
    for r in q:
        if r in w:
            return True
        else:
            return False
    print(r)
set(q).difference(w)

import string
q='abcd'
w='1234'
e=translator(r=string.digits)
print(e)
'''
q='abcdxyz'
w,e,*r,t=q
print(w,e,r,t)
print(*r)
#三目运算符
'''y='asd'

u=y if u=="asd" else u='dsa'
print(u)'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fab(5)
print('----------')
def ass():
    for i in range(5):
        yield i
def ads():
    yield from range(5)

a=ads()
for i in a:
    print(i)

print('_______')
import heapq
f=[1,6,3,4,5]
print(heapq.nlargest(2,f))
#print(heapq.heappop(f))
print(heapq.heapify(f))
print(f)
print('------------------不报错字典----------------------')
from collections import defaultdict
g=defaultdict(set)
h=defaultdict(int)
j=defaultdict(list)
l=defaultdict(dict)
j['a'].append(1)#添加元素


print(g,h,j,'--------',l['name'])

k=dict()
#print(d['name'])
print('---------------------------')
j['b'].append(2)
j['c'].append(3)
def k():
    k=j.values

print(j)
print(min(j),min(j.values()))
print('----------------')
print(j.items())
z={'a':2,'d':5,'e':8}
l.update(z)
print(j)
v={'f':10}
l.update(v)
print(l)
print(z.keys() - l.keys())
print(z.keys())#键视图的集合操作
#num = 1 if param > 10  else 2 if param == 10 else 0
'''if param > 10 :
	num = 1
elif  param == 10:
	num = 2
else:
	num = 0'''
print('---------------')








































