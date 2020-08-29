

for i in range(20):
    for base in 'bdX':  # 2進数　10進数　16進数でループを回す
        print('{:5{base}}'.format(i, base=base), end=' ')
    print()
