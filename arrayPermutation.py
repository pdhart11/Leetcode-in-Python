class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)):
            new.append(nums[nums[i]])
        return new
