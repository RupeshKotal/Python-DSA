n = [5,4,3,5,6,5,7,8,1,2,3,4,5,4,9,7,6,5,4,6]

m = [10, 56,4,2,3,2,67,45,90,6,8,7,2,4,6,7,2,3,5]


hashlist = [0] * 11

for val in n:
    hashlist[val]+=1


for num in m:
    if num > 10 or num < 1:
        print(num,0)
    else:
       print(num, hashlist[num]) 
   