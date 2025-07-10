#!/usr/bin/python3

word = "Ronaldo"
count_letter={}
repited_letter=""

for letter in word:
    if letter in count_letter:
        count_letter[letter] += 1
    else:
        count_letter[letter] = 1

repited_letter = max(count_letter)
new_word = word[:len(word)//2] + ''.join(repited_letter) + word[len(word)//2:]

print(word)
print(new_word)
        

