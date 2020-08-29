import functools


# クロージャーのような記述をもっと簡易的に記載する方法

def f(x, y):
    return x + y

# def outer(x,y):
#     def inner():
#         return x + y
#     return inner


# f = outer(10, 20)
def task(f):
    print('start')
    print(f())


p = functools.partial(f, 10, 20)
task(p)
