
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # own
        near = 0
        val = 0
        for i in range(len(nums)):
            if (nums[i] == target):
                return i
            elif (nums[i] < target):
                near = i
                val = nums[i]
        if(val == 0):
            return near
        return near+1
