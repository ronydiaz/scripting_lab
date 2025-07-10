#!/usr/bin/env python3

the_list = [1, 4, 5, 13, 9, 54, 7]

print(the_list)
for element in range(len(the_list)//2):
    the_list[element], the_list[-element-1] = the_list[-element-1], the_list[element]

print(the_list)




