class Solution:
    def __init__(self) -> None:
        pass
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        v = nums1 + nums2
        length = len(v)
        sum = 0
        median = 0
        for i in range(length):
            sum = sum + v[i]
            for j in range(0, length-i-1):
                if v[j] > v[j+1]:
                    v[j], v[j+1] = v[j+1], v[j]

        divisor = length % 2
        if length == 1:
            median = sum
        elif divisor == 0:
            mid_first = int(length/2)
            mid_second = int((length/2) - 1)
            median = (v[mid_first] + v[mid_second]) / 2

        else:
            median = v[int(((length - 1)/2 + (length + 1)/2)/2)]
        return median
