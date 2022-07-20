class Solution:
    def search(nums: List[int], target: int) -> int:
        i = 0
        end = len(nums) -1
        while i <= end:
            mid = (i + end) // 2
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                i = mid - 1
            else:
                return mid
        return -1
