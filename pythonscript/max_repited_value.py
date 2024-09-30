#!/usr/bin/env python3

the_list=[4,6,4,8,3,4,3,7,9,45,15,2,4]
dic_count={}

for element in the_list:
    if element in dic_count:
        dic_count[element] = 1 + dic_count[element]
    else:
        dic_count[element] = 1

print(f'The max repited value from {the_list} is: {max(dic_count.values())}')
