class Solution:
    def minimumSum(self, num: int) -> int:
        sorted = []
        num = str(num)
        for i in range(len(num)):
            sorted.append(num[i])
        sorted.sort()
        part1 = sorted[0] + sorted[2]
        part2 = sorted[1] + sorted[3]
        return int(part1) + int(part2)
