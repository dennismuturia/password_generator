#/usr/bin/python
'''
Author: Dennis Muturia
version: v1.0.0
'''
import sqlite3
import connect
from random import randint

def randomPassword(password_length=5):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','0','1', '2', '3', '4','5','6','7','8','9']
    password = ''
    i = 0
    while(i < password_length):
        rand = randint(0,len(letters) - 1)
        password += letters[rand]
        i += 1
    return password

print(randomPassword())