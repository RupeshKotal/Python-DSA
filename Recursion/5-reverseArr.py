num = [1,2,3,4,5,6,7,8,9,10]

def revArr(num,left,right):
    if left >= right:
        return
    
    num[left],num[right] = num[right], num[left]

    return  revArr(num,left+1,right-1)


revArr(num,0,9)

print(num)