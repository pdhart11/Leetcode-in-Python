class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new = 0
        max = nums[0]
        for i in range(len(nums)):
            new += nums[i]
            if new > max:
                max = new
            if new < 0:
                new = 0
        return max
