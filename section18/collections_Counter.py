import re
import collections

l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
print(c.most_common(2))
print(sum(c.values()))

with open('section18/collections_Counter.py', 'r') as f:
    # \w 任意の英数字	[a-zA-Z0-9_]
    # +  繰り返し文字列
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))
