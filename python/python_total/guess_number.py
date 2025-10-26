#!/usr/bin/env python3

from random import *

name = ""
number= 0 
random_number = randint(1,100)
try_counter = 1
print(random_number)

while ( (not isinstance(name,str)) or (name.isdigit()) or (len(name) <= 0) ):

    name = input("What's your name: ")

    if name.isdigit():
        print("Invalid Input, name can't be a digit")

print(f"Well, {name}, I've tough a number between 1 and 100. You have only eight tries to guess which is the number")


while ( (not isinstance(number,int)) or (number <= 0) or (number > 100) or (try_counter <= 8)):

    try:
        number = int(input("Introduce a number between 1 and 100: "))

        if ((number <=0) or (number > 100)):
            print(f"Invalid input, the number must be between 1 to 100, {number} is out of range")

        elif number < random_number:
            print(f"Wrong answer!, {number} is minor than secret number")

        elif number > random_number:
            print(f"Wrong answer!, {number} is major than secret number")

        else:
            print(f"Correct!, {number} is the right number, you've won on your {try_counter} try")
            break

    except ValueError:
        print("Input must be an valid interger")


    if try_counter == 8:
        print(f"You've lost, the right answer is {random_number}") 

   
    try_counter += 1




