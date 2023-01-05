from math import sqrt

edge = float(input().strip())

area = 2 * sqrt(3) * edge ** 2
volume = 1 / 3 * sqrt(2) * edge ** 3
print(round(area, 2), round(volume, 2))
