n = [5,4,3,5,6,5,7,8,1,2,3,4,5,4,9,7,6,5,4,6]

m = [10, 56,4,2,3,2,67,45,90,6,8,7,2,4,6,7,2,3,5]


freq = {}

num = len(n)

for num in n:
    freq[num] = freq.get(num,0) + 1

for num in m:
    if num > 1 and num < 10:
        print(f' {num} = {freq.get(num,0)}')
    else:
        print(f' {num} = 0')


