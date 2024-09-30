word1='Listen'
word2='SilenT'

def anagram(w1,w2):
    w1 = w1.replace(' ','').lower()
    w2 = w2.replace(' ','').lower()

    print(w1)
    print(w2)

    w1 = list(w1)
    w2 = list(w2)
    w1.sort()
    w2.sort()
    if len(w1) != len(w2):
        return False
    
    if w1 == w2:
        print(f'{w1}\n{w2}')
        return True

print(anagram(word1, word2))
