"""
Test Test #################################################
"""
animal = 'cat'

def f():
    print(animal) # ファイル内有効のため表示可能


def f2():
    """Test func doc"""
    print(f2.__name__)
    print(f2.__doc__)
    animal = 'dog'
    print('after',animal)
    print('local:', locals()) #関数内の変数を全部表示する
    print('global:', globals())


f()

f2()
print(animal)

print('global2:', globals())


