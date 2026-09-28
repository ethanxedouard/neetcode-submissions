class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        cur = 0
        for n in nums:
            cur += n
            prefix.append(cur)

        for i in range(len(nums)):
            l = prefix[i-1] if i > 0 else 0
            r = prefix[-1] - prefix[i]
            if l == r:
                return i
        return -1