#!/usr/bin/env python3

'''
This program shall receive a list of numbers and count each of them to detect which one is the most repited one
'''


the_list=[4,6,4,8,3,4,3,7,9,45,15,2,4]
num_count={}

for element in the_list:
    if element in num_count:
        num_count[element] = 1 + num_count[element]
    else:
        num_count[element] = 1

max_repited=max(num_count, key=num_count.get)

print(f'The max repited value from {the_list} is: {max_repited}')
