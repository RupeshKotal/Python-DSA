from math import sqrt

class Solution:
    def countFactors (self, N):
        arr = []

        for i in range(1,int(sqrt(N))+1):
            if N%i==0:
                arr.append(i)
                if N//i != i:
                  arr.append(N//i)

            
        return(len(arr))