import string
import os

print(os.getcwd())

with open('email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)