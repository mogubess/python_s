##Pypi (サードライブラリ)提供ライブラリ
#termcolor
import collections
import sys
from termcolor import colored

print('test')
print(colored('test', 'red'))

#print(help(colored))

#importする際の注意
#importはひとつずつ、アルファベット順
#標準ライブラリとサードパーティのライブラリは一行あける
#自作や自分のチームのライブラリ(パッケージ)をimportする場合は、もう一行あける
#自分の関数を最後にする

print(sys.path)