#!/usr/bin/env python3

the_list = [34, 2, 4, 25, 9, 6, 7]
temp_var=0
print(the_list)

for list_check in range(len(the_list)-1):
    for element in range(len(the_list)-1-list_check):
        if the_list[element] > the_list[element+1]:
            the_list[element], the_list[element+1] = the_list[element+1], the_list[element]

print(the_list)

