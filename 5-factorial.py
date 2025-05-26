# n=7
# num = n

# output = []

# for i in range(1 ,num+1):
#  if num % i == 0:
#   output.append(i)

# print(output)


## Optimal

from math import sqrt

n = 36

num = n

result = []

for i in range(1, int(sqrt(num)) + 1 ):
    if num%i == 0:
        result.append(i)
        if num//i != i:
            result.append(num//i)


print(result)