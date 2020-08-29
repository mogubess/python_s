def say_somathing():
    s ='hi'
    return s

result = say_somathing()
print(result)

#リストをデフォルト引数で初期化しない

#位置引数のタプル化
#wordに最初の引数が入る
#argsに残りの引数がリスト化されてはいる
def say_somthing2(word ,*args):
    print(word)
    for arg in args:
        print(arg)

say_somthing2('Hi', 'Mike', 'Nance')

t = ('Mike', 'Nancy')
say_somthing2('Hi', *t)

#キーワード引数の初期化 順序は重要
def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana','apple','orange',entree='beef',drink='coffee')

#docstring


#関数内関数
#繰り返し使うような処理


#クロージャー
def outer(a,b):

    def inner():
        return a+b

    return inner

f = outer(1,2)
r = f()
print(r)

#デコレータ
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a,b):
    return a + b

r = add_num(10,20)
print(r)

#デコレータを２つ並べると先に定義されている、デコレータを呼ぶ




