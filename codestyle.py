s = ('aaaaaaaaaaaaaaaaaa'
'bbbbbbbbbbbbbbbbbbbb')


#80文字以上で次にいく
x = 10
if x < 0:
    print('nega')
elif x == 10:
    print('10')

a=5
b=10

### VSCODEでのデバッグ方法を調べる
#a b
if a == b:
    print('equal')

if a > 0 & b > 0:
    print(a)

#notを数値の比較で使うのはできればさけたい



#while elseはwhileをbreakで抜けなければ実行される
#for elseもおなじ

#range

for _ in range(10):
    print('hhh')

for i ,fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day,fruit,drink)

#lamda ラムダ


lam = ['mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
#ample_func = lambda word: word.capitalize()

#change_words(lam, sample_func)
change_words(lam, lambda word: word.capitalize())
change_words(lam, lambda word: word.lower())


#ジェネレータ

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

gg = greeting()

print(next(gg))
print(next(gg))
print(next(gg))

def counter(num=10):
    for _ in range(num):
        yield 'run'


#リスト内包表記
t  = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]

print(r)

#辞書包括表記（内包表記）
#zipで回して、辞書を作成することと同じ
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x,y in zip(w,f):
    d[x] = y

print(d)

d = {x:y for x,y in zip(w,f)}
print(d)

#集合内包表記

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

#ジェネレータ内包表記
def g34():
    for i in range(10):
        yield i
    
g333 = (i for i in range(10) if i %2 == 0 )
print(type(g333))

for xx in g333:
    print(xx)