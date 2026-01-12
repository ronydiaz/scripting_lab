#!/usr/bin/env python3

from random import *

with open('words.txt','r') as file:
    data = list(file.readlines())

#print(data)

flag = True

word = choice(data)
word =  word.lower()
word_copy = "_ " * len(word)
print(f"Your word is: {word_copy}")

life_counter = len(word)

while(flag and live_counter > 0):
    
    char = input("Summit a letter: ")
    
    if "char" in word:
        pass

    else:
        live_counter -= 1

    if live_counter == 0:
        print("You lost")
    else:
        print(f"Missing Lifes: {live_counter}")
