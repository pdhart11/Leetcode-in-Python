class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        result = False
        myString = ""
        for i in range(len(s)):
            for j in range(index, len(t)):
                if s[i] == t[j]:
                    index = j + 1
                    myString = myString + s[i]
                    break
        if myString == s:
            result = True
        return result
