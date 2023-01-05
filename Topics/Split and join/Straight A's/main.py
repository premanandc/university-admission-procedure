# put your python code here
grades = input().strip().upper().split()

a = [grade for grade in grades if grade == 'A']

print(round(len(a) / len(grades), 2))
