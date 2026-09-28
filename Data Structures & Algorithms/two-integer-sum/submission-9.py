class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            rem = target - n
            if rem in prev:
                return [prev.get(rem), i]
            prev[n] = i