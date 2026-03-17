#!/usr/bin/env python3

from random import *

with open('words.txt','r') as file:
    data = list(file.readlines())

#print(data)

flag = True

word = choice(data)
word =  word.lower()
word_copy = "_ " * len(word)
print(f"Your word is: {word}")

life_counter = len(word)

while(flag and life_counter > 0):
    
    char = input("Summit a letter: ")
    
    if char in word:
        
        indexes = [i for i, x in enumerate(word) if x == char]
        print(indexes)

        for i in indexes:
            word_copy = word_copy[:i+1] + word[i] + word_copy[i:]

        print(word_copy)


    else:
        life_counter -= 1

    if life_counter == 0:
        print("You lost")
    else:
        print(f"Missing Lifes: {life_counter}")
