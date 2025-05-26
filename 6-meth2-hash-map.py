nums = [12,56,23,23,56,23,44,53,44,44,1,21,1,34,34,21,12]

hashMap = {}

for i in nums:
    hashMap[i] = hashMap.get(i,0) + 1



print(hashMap)