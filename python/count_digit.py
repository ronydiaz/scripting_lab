#!/usr/bin/env python3

'''
This program get a string as input for identifying and count the total of digits on the word
'''

user="01_Ronaldo245"

def count_digit(the_string):
    digit_counter=0

    for char in the_string:
        if char.isdigit():
            digit_counter += 1

    return digit_counter

print(f"The word is {user} and contain {count_digit(user)} digits")



