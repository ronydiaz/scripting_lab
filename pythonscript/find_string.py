#!/usr/bin/env python3

user_list=[1,4,'5',4,'25',7,26,'45']

def find_char(the_list):

    strings=[]
    
    for element in the_list:
        if isinstance(element, str):
            strings.append(element)
    
    return strings


print(find_char(user_list))
