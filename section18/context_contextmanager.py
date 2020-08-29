import contextlib

# デコレータに関連するライブラリ


# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag


# @tag('h2')
# def f(content):
#     print(content)

# #f = tag('h2')(f)


# f('test')

# 関数のデコレータを使う場合
@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))


@tag('h2')
def f(content):
    print(content)


f('test')

# withステートメントを使う場合


def f2():
    print('test0')
    with tag('h2'):
        print('test')


f2()
