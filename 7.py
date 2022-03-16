

thestring='12345'
thelist=list(thestring)
for c in thestring:
    print(c)
print(thelist)

#列表推导式
lx=[c*2 for c in thestring]
print(lx)
print('_________________')
def q(w):
    return w*2


#map函数
e=list(map(q,[1,2,3,4,5,6]))#与list函数混用
print(e)
print(type(e))
#map（函数，列表）
r=set('aassddffgg')
t=set('ssddffgg')

print(''.join(r&t))
print('-----------------')
print(ord(u'\u2020'))
print(chr(8224))
print(list(map(ord,'操')))
print('---------')
    #lambda函数
y=(lambda u,i,o:u*i*o)(2,3,4)
print(y)


def sum(x, y):
    return x + y

p = lambda x,y:x+y
print(p(4,6))
print('--------------')
#遍历拼接
u=['1','2','3','4','5']
i=['a','b','c','d','e']
for o in range(0,5):
    print(u[o],i[o])
print('-------')
for p in zip(u,i):
    print(p)

print('--------')
anobj='adsdvd'
def isStringLike(anobj):
    try:
        anobj + 'a'
    except:
        return False
    else:
        return True
print(type(anobj),anobj)
#字符串具有可大小写和可追加属性，用于判断对象是否是字符串类型
print('------------')
print('user'.center(20,'='))

print('user'.rjust(20,'='))
print('_________')
g=('xa   asdf    ax')
h=g.strip('x'+'a')
print(h.strip( ))#rstrip和lstrip
print('--------')
k=['sa','la','ka']
print(''.join(k))
l='%s ajshd %s sdv'%('yui','sdf')#格式化操作符号--%
print(l)
'''z=g+l+'erf'

print(z)
x='a-'
v='123456'
m=''
for n in v:
    n+=x
    m+=n
obj=list(m)

print(obj)'''















































