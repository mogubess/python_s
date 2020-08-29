try:
    from sakkai.talk import * #古いVersionはこれで
except ImportError:
    from talk import animal   #新しいVersionはこれで記載するみたいな
    from talk import human


print(animal.sing())

print(human.sing())