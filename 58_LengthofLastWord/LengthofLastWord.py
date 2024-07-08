
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        print(len(s[-1]))
        return len(s[-1])
        # count = 0
        # for i in range(0,len(s)):
        #     if not s[-i] == ' ':
        #         count += 1
        # return count
