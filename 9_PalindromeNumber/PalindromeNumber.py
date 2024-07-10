class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev = 0
        while num > 0:
            rev = (rev * 10) + int(num % 10)
            num = int(num / 10)
        if rev == x:
            return True
        return False
        # effeciant
        # if x < 0 or (x%10==0 and x!=0):
        #     return False
        # revertedRightHalf = 0
        # while x > revertedRightHalf:
        #     remainder = x%10
        #     revertedRightHalf = revertedRightHalf * 10 + remainder
        #     x = x//10
        # # print(x, revertedRightHalf)
        # return x==revertedRightHalf or x==revertedRightHalf//10
