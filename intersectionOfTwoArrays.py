class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            for j in range(0, len(nums1)-i-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
        
        for i in range(len(nums2)):
            for j in range(0, len(nums2)-i-1):
                if nums2[j] > nums2[j+1]:
                    nums2[j], nums2[j+1] = nums2[j+1], nums2[j]
        new = []
        i = j = 0
        while True:
            try:
                if nums1[i] > nums2[j]:
                    j += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    new.append(nums1[i])
                    i += 1
                    j += 1
            except IndexError:
                break
        return new
