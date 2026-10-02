class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        activeSub = set()
        maxSum = 0
        left = 0

        for right in range(len(s)):
            while s[right] in activeSub:
                activeSub.remove(s[left])
                left += 1
            activeSub.add(s[right])
            maxSum = max(maxSum, len(activeSub))

        return maxSum