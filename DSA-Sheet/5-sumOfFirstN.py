class Solution:
    def sumOfSeries(self,n):
        #code here
        
        if n < 1 or n >200:
            return 0
        if n == 1:
            return 1
            
        return n**3 + self.sumOfSeries(n-1)
