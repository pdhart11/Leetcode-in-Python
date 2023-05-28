class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        beginning = 0
        end = len(s)-1
        vowels = 'aeiouAEIOU'
        while beginning < end:
            if s[beginning] in vowels and s[end] in vowels:
                (s[beginning], s[end]) = (s[end], s[beginning])
                beginning += 1
                end -= 1
            elif s[beginning] not in vowels:
                beginning += 1
            elif s[end] not in vowels:
                end -=1 
        return ''.join(s)
