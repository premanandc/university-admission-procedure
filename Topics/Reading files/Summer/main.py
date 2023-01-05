#  write your code here 
file = open('/Users/prem/Downloads/hyperskill-dataset-73688790.txt')
count = 0
for line in file:
    print(line)
    if line.strip() == 'summer':
        count += 1
print(count)
