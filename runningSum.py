class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        my_array = []
        count = 0
        for i in range(len(nums)):
            count = count + nums[i]
            my_array.append(count)
        return my_array
