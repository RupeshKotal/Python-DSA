def func(sum,i,n):
    if i > n:
        print(sum)
        return
    
    func(sum+i,i+1,n)


print(func(0,1,10))