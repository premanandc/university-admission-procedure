# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
children = dict.fromkeys(groups)
for i in range(int(input())):
    children[groups[i]] = int(input())
print(children)
