#!/usr/bin/python3

import random

random_list=[random.randint(1,10) for x in range(10)]
sorted_list=sorted(random_list)

print(sorted_list)

def remove_duplicated_numbers(nums: list[int]) -> int:

    k=0
    i=0

    while i < len(nums) -1:

        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1

    print(nums)

    k=len(nums)
    return k


remove_duplicated_numbers(sorted_list)
