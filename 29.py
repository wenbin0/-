q=['a','b','c','d','e','a','b','c']

w=slice(1,3)
print(q[w])
#slice函数添加元素
q[w]=[1,2]
print(q)
from collections import Counter
e=Counter(q)
t=[10,20,100]
y=Counter(t)
u=y+e
print(e)
print(u)
#根据关键字排序列表
'''from collections import defaultdict
o=defaultdict(dict)
o.setdefault('a','[1,2,3]')
print(o)
o.setdefault('b','[2,3,5]')
o=[{'a':2,'b':3,'c':1}]
from operator import itemgetter
i=sorted(o,key=itemgetter(a))'''
a='aaabbbcccaaaddd'
from itertools import groupby
for a,b in groupby(a):
    print(a,list(b))
#按条件过滤
s=[1,3.5,4,-2,9.6,-8]
print([n for n in s if n>0])
print('-------------')

def d(h):
    try:
        f=int(h)
        return True
    except ValueError:
        pass
g=list(filter(d,s))
print(g)





















