import abc #抽象クラスのパッケージ
           #抽象クラスはコードスタイルで推奨されていない、なくてもつくれるよねっこと

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractclassmethod
    def drive(self):
        pass

#継承先にクラスは必ず、drive関数を実装する
#propertyをつくっておけばsetterで値判定が可能になる



class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == 'Hide':
            raise IndexError
        else:
            self.__name = value

    @name.deleter
    def name(self):
        del self.__name


adl = Adult()

adl.name = 'Hideo'
print(adl.name)
