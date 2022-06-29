class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if s == t:
            return True
          
s = "anagram"
t = "nagaram"
print(Solution.isAnagram(s, t))
