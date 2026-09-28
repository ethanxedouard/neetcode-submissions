class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) > len(nums) / 2:
                return n
        