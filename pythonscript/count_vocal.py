#!/usr/bin/env python3

import sys

vocals=['a','e','i','o','u']
vocals_in_word=[]


def vocal_counter(word):

    vocal_cnt=0

    for letter in word:
        if letter in vocals:
            vocals_in_word.append(letter)

            vocal_cnt += 1

    print(f"There are {vocal_cnt} vocales: {vocals_in_word}")

try:
    vocal_counter(sys.argv[1])
except:
    print("There were not a submitted a word")
