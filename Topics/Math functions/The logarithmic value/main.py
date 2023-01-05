from math import log

n1, n2 = int(input().strip()), int(input().strip())

out = round(log(n1, n2), 2) if n2 > 1 else log(n1)
print(round(out, 2))
