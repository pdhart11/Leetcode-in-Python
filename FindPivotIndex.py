class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        beginSum = 0
        endSum = 0
        for i in range(len(nums)):
            endSum = endSum + nums[i]
        for i in range(len(nums)):
            endSum = endSum - nums[i]
            if beginSum == endSum:
                return i
            beginSum += nums[i]
        return -1
