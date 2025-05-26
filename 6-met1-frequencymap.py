nums = [12,56,23,23,56,23,44,53,44,44,1,21,1,34,34,21,12]

frequency = dict()  #{}

for i in range(0,len(nums)):
    if nums[i] in frequency:
        frequency[nums[i]] +=1
    else:
        frequency[nums[i]] = 1


print(frequency)