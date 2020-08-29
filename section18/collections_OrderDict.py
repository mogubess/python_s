import collections

d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}

# OrderDictに入れるときに、ソートで順番を変更して、いれることができる
od = collections.OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

print(od)
