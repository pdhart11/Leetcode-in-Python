class Solution:
    def countAsterisks(self, s: str) -> int:
        barCount = 0
        asterisks = 0
        for index in range(0, len(s)):
            if s[index] == '|':
                barCount += 1
            if barCount % 2 == 0:
                if s[index] == '*':
                    asterisks += 1
        return asterisks
