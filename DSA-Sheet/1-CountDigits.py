#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        
        count = 0
        
        for num in str(n):
            if num == '0':
                continue
            if n%int(num) == 0:
                count+=1
        return count