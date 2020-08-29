import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

m = collections.ChainMap(a, b, c)
print(m)
print(m.maps)
m.maps.reverse()
print(m.maps)
m.maps.insert(0, {'c': 'CCCCCC'})
print(m.maps)
print(m['c'])
del m.maps[0]
print(m.maps)
print(m['c'])
