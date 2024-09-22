#!/usr/bin/env python3

bin_list=[0,0,0,1,1,0,1,0,1]
print(bin_list)

for element in bin_list:
    extract_element = 0
    if element == 1:
        bin_list.remove(element)
        bin_list.append(element)

print(bin_list)
