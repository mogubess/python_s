#Exception hierarchy
l = [1,2,3]

#i = 5
i=1
#del l

try:
    l[i]
    #    () + l
except IndexError as exc:
    print("Dont't worry: {}".format(exc))
except NameError as exc:
    print(exc)
except Exception as exc:
    print('other:{}'.format(exc))
else:
    print('done') #例外が発生しなかったときだけ実行される
finally:
    print('clean up') # 必ず実行される

print("last")

#raise IndentationError('test error') 例外を発生させる方法

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('UpperCaseError:{}'.format(exc))
finally:
    print('final')

