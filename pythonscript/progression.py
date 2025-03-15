#!/usr/bin/env python3

print("This code will take a number as input and separete theirs digits and multiply the recursively until get one digit")

number=input("Submit a number: ")
regresion_cnt=0

def progression(int_number):

    global regresion_cnt
    number_list = list(int_number)
    result = int(number_list[0])
    print(number_list)

    if len(number_list) <= 1:
        print(f"Total Iterations: {regresion_cnt}")
    else:
        for i in range(1, len(number_list)):
            result *= int(number_list[i])

        regresion_cnt += 1
        progression(str(result))


progression(number)

