nums = [90,3,4,6,2,4,7,89,53,22,25,6,7,43,3,46]

def partiton(nums, low, high):
    piviot = nums[low]
    i = low
    j = high

    while i < j:
        while nums[i] <= piviot and i <= high - 1:
            i+=1

        while nums[j] > piviot and j >= low + 1:
            j-=1

        if i < j:
            nums[i],nums[j] = nums[j],nums[i]

    nums[low],nums[j] = nums[j],nums[low]

    return j

def quick_sort(nums,low,high):
    if low < high:
        p_index=partiton(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)


quick_sort(nums,0,len(nums)-1)

print(nums)

