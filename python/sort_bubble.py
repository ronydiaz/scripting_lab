#!/usr/bin/env python3

'''
Classic program for sorting using bubble sort algorithm
'''

import random

the_list = [random.randint(2,100) for i in range(10)]
print(the_list)

for list_check in range(len(the_list)-1):
    for element in range(len(the_list)-1-list_check):
        if the_list[element] > the_list[element+1]:
            the_list[element], the_list[element+1] = the_list[element+1], the_list[element]

print(the_list)

