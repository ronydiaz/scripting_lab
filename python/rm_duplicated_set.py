#!/usr/bin/python3


import random

random_list=[random.randint(1,20) for x in range(10)]
print(f"Random List: {random_list}")


def remove_duplicated_elements(numbers: list[int]) -> list:

    seen_numbers=set([])
    repeated_numbers=set([])
    not_repeated=[]

    for element in numbers:

        if element in seen_numbers:
            repeated_numbers.add(element)    

        else:
            seen_numbers.add(element)

    print(f"All numbers: {seen_numbers}")
    print(f"Repeated numbers: {repeated_numbers}")

    for number in seen_numbers:
        
        if number not in repeated_numbers:
            not_repeated.append(number)

    return not_repeated

print(f"Not repeated numbers: {remove_duplicated_elements(random_list)}")

