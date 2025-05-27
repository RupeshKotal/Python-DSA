class Solution:
    def isPalindrome(self, x: int) -> bool:
     
     num = x

     result = 0

     if x < 0:
        return False

     if x > 0:
        last = num%10
        result+= last

     return True if x == result else False

     if result < -2 **31 or result > 2 ** 31 -1:
        return 0



        