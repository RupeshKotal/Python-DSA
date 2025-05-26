from math import sqrt

num = 78

n = num

result = []

for i in range(1, int(sqrt(n)) + 1):
  if n%i == 0:
    result.append(i)
    if num//i != i:
      result.append(num//i)

result.sort()
print(result)