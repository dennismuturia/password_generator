#/usr/bin/python
from random import randint

def randomPassword(password_length=5):
    letters = ['a', 'b', 'c', 'd', 'e','0','4']
    password = '';
    i = 0
    while(i < password_length):
        rand = randint(0,len(letters) - 1)
        password += letters[rand]
        i += 1
    return password

print(randomPassword())