class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAnagram = True
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in t and s.count(s[i]) == t.count(s[i]):
                    isAnagram = True
                else:
                    return False
            if isAnagram == True:
                return True
            else:
                return False
        else:
            return False