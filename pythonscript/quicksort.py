#!/usr/bin/env python3

import random

the_list=[random.randint(1,100) for x in range(10)]
print(the_list)

def sort(arg_array):

    # L and R temp arrays
    l_array=[]
    r_array=[]
    pivote=0

    if len(arg_array) < 1:
        return arg_array
    else:
        pivote=arg_array.pop()

    for x in arg_array:
        if x < pivote:
            l_array.append(x)
        elif x > pivote:
            r_array.append(x)
    
    return sort(l_array) + [pivote] + sort(r_array) 


print(sort(the_list))
