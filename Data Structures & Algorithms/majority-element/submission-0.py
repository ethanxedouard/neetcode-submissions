class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rank = {}

        for n in nums:
            if n in rank:
                rank[n] += 1
            else:
                rank[n] = 1
        
        total_sum = len(nums)

        for i in rank:
            if rank.get(i) > total_sum / 2:
                return i