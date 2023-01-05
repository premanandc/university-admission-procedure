# put your python code here
words = input().strip().lower().split()
out = {word: words.count(word) for word in words}
print('\n'.join(f'{k} {v}' for k, v in out.items()))
