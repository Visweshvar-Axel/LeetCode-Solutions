
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        num = x
        rev = 0
        while(num > 0):
            rev = (rev * 10) + int(num % 10)
            num = int(num / 10)
        if (rev == x):
            return True
        return False
