word1 = input()
word2 = input()

print(''.join(a + b for a, b in zip(word1, word2)))
