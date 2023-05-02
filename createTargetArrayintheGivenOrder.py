class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        targetArray = []
        for indexElement in range(len(index)):
            targetArray.insert(index[indexElement], nums[indexElement])
        return targetArray
