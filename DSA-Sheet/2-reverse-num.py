class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        num = abs(x)
        
        result = 0
        while num > 0:
            last = num%10
            result = (result*10)+last
            num = num//10

        final = result * sign
        if final < -2**31 or final > 2**31 - 1:
            return 0
        return final

        

