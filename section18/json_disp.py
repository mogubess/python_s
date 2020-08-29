import json

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
print(json.dumps(l, indent=4))
print(json.dumps(d, indent=4))
