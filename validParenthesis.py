class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        while len(s) > 0:
            length = len(s)
            s = s.replace('()','').replace('[]','').replace('{}','')

            if len(s) == length:
                return False
        return True
