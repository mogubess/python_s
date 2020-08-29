##sorted

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print(sorted(ranking))#ランキングのキーでソート

print(sorted(ranking, key=ranking.get))#ランキングのバリューでソート

print(sorted(ranking, key=ranking.get, reverse=True))#ランキングのバリューでソート 降順

##complex 複素数
c = 3 + 4j

print(c)
print(type(c))
# (3+4j)
# <class 'complex'>


# c = 3 + j
# NameError: name 'j' is not defined

c = 3 + 1j

print(c)
# (3+1j)


c = 3j

print(c)
# 3j


c = 3 + 0j

print(c)
# (3+0j)


#実部、虚部は浮動小数点float型で指定できる。指数表記などでもOK。

c = 1.2e3 + 3j

print(c)
# (1200+3j)

#complex型のコンストラクタで生成することもできる。complex(実部, 虚部)のように指定する。
c = complex(3, 4)

print(c)
print(type(c))
# (3+4j)
# <class 'complex'>