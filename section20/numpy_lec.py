import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0][0])
print(a.shape)  # 次元毎の要素数(3,3)1次元、2次元

print(a.ndim)   # 次元数

print(a.dtype.name)  # 変数の型(int64)

print(a.size)  # 大きさ

print(np.arange(0, 30, 5))  # 0から30まで5ずつの配列

print(np.arange(0, 2, 0.3))  # 0から2まで0.3ずつの配列を生成

print(np.zeros((3, 4), dtype=np.int16))  # 3次元で要素数4の配列を作成
# np.ones
# np.nan

# 0から2の間に9個分の値を取得してくれる
print(np.linspace(0, 2, 9))

# 要素数4個の3次元配列を２個つくる
a = np.arange(24).reshape(2, 3, 4)
print(a)

# 表示の限界値を変更する設定関数
# np.set_printoptions(threshold=10000)
print(np.arange(10000).reshape(100, 100))

# 配列どうしの結合を表示することもできるよ
#np.append(x, y)

x = np.arange(0, 10, 2)
y = np.arange(5)
z = np.arange(0, 100, 20)

print(np.append(x, y))

# vertical
print(np.vstack([x, y, z]))

# horizontal
print(np.hstack([x, y, z]))

# 配列同士の剰余除算
