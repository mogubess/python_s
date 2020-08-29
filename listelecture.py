#### list []
#### IndexError

# index 検索

# count


l = [1,2,3,4]

l.insert(0,100)

#sort sort(reverse=True)

#リストのコピー
i = [1,2,3,4,5]
k = i
j = i.copy()
j[0] = 100
print('j=',j)
print('i=',i)

print(id(i))
print(id(k))

### append/pop

#### tuple ()
#t=1,とすると、タプルになる()としても,をつけないと数値になる

### アンパッキング
a=100
b=200
a,b=b,a
new_tuple = 1,2,3
x,y,z = new_tuple
print(x,y,z,sep='#')
#
print(a,b)


### dict {:}
da = dict([('a',10),('b',20)])
print(da)

#keys

#values

#update
#d.update(d2)

#get

#pop

#del

#clear

#in

#辞書のコピー

x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)

dx = {'a':1}
dy = dx.copy()
dy['a'] = 1000
print(dx)
print(dy)

### for文で展開 items
dxxx = {'a':1, 'b':200}
print(dxxx.items())

for k, v in dxxx.items():
    print(k, ':', v)



###set 集合 {}キーがない

aa = {2,3,6,7}
bb = {1,2,3,4,5,6}

print(aa-bb)
print(aa & bb)
print(aa ^ bb)

#add
aa.add(1)
print(aa)
aa.add(1)#変わらない

#remove

#clear


"""
test
test
test
"""
