word = 'python'

print(word[0])

word = 'j' + word[1:]
print(word)

#startswith

#find

#rfind
#２個めの文字を検索するには

#count

#capitalize

#title

#upper

#lower

#replace

#str 文字列への型変換

#3.6 以降であればformatではなくf-stringを使っている

a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
 
name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')