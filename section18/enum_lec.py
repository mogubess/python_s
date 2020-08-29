import enum

db = {
    'stack1': 1,
    'stack2': 2,
}


# このデコレーションは同一の値を持つ列挙子を許容しない
@enum.unique
class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3


if Status(db['stack1']) == Status.ACTIVE:
    print('shutdownS')
elif Status(db['stack1']) == Status.INACTIVE:
    print('terminateS')


# integer型のenumクラス　値の参照で、Statusで変換する必要がない
class StatusInt(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3


if db['stack1'] == StatusInt.ACTIVE:
    print('shutdown')
elif db['stack1'] == StatusInt.INACTIVE:
    print('terminate')


# flg型のenmクラス フラグなので、6は4と2の組み合わせらしい
class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1
    Z = 6


print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W | Perm.X))
RWX = Perm.R | Perm.W | Perm.X
print(Perm.W in RWX)
print(Perm.Z in RWX)
