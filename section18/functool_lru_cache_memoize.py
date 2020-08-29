
# 計算結果を保存しておけば、毎回計算に時間がかかることがないようにできる
import functools


def memoize(f):
    memo = {}

    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
            # print('hit')
            # print(memo)
        return memo[n]
    return _wrapper


@memoize
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * 1
    return r


for i in range(10):
    #    print(long_func(i))
    long_func(i)

print('next run')
for i in range(10):
    #    print(long_func(i))
    long_func(i)


# lru_cacheはmemoizeで行っていることを実施するパッケージ
# 引数で渡された結果をキャッシュしてくれる、最大サイズを超えたら、古いのから消去
@functools.lru_cache(maxsize=5)
def long_funcC(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_funcC(i))

print(long_funcC.cache_info())
long_funcC.cache_clear()


print('next_run')

for i in reversed(range(10)):
    print(long_funcC(i))

# CacheInfo(hits=0, misses=10, maxsize=5, currsize=5
print(long_funcC.cache_info())
