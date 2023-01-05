# read sums.txt
with open('sums.txt') as file:
    for line in file:
        print(sum([int(x.strip()) for x in line.split()]))
