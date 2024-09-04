#!/usr/bin/env python3

import sys

def palindrome(word):
    inverted_word=""
    word = word.replace(" ","").lower()
    
    for character in word:
        inverted_word = character + inverted_word
    
    if word == inverted_word:
        print(f"{word} is palindrome of {inverted_word}")
    else:
        print(f"{word} is not a palindrome of {inverted_word}")

palindrome(sys.argv[1])
