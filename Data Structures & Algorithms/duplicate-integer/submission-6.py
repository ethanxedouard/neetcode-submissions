class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        usedLetters = []

        for num in nums:
            if num in usedLetters:
                return True
            else:
                usedLetters.append(num)
        return False
        