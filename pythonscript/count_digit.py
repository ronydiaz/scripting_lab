#!/usr/bin/env python3

user="01_Ronaldo245"

def count_digit(the_string):
    digit_counter=0

    for char in the_string:
        if char.isdigit():
            digit_counter += 1

    return digit_counter

print(count_digit(user))



