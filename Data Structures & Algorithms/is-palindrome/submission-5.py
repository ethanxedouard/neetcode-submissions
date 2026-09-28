class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for i in s:
            if i.isalnum():
                newStr += i.lower()
            
        left = 0
        right = len(newStr) - 1

        while left < right:
            if newStr[left] == newStr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True