#!/usr/bin/env python3

text = input("Introduce a text, pharagrap or phrase: ")
text_lower = text.lower()
letters = list(input("Introduce three letters: ").lower())

letter_cnt = {}
words_cnt = text.split()
inverted_text = " ".join(words_cnt[::-1])
python_check = "Python" in text

for char in text_lower:

    if char in letters:
        if char in letter_cnt:
            letter_cnt[char] += 1
        else:
            letter_cnt[char] = 1



print(letter_cnt)
print(len(words_cnt))
print(text[0],text[-1])
print(inverted_text)
print(python_check)
