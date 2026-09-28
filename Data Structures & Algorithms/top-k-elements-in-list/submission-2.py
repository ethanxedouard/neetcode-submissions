class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for i in range(k):
            max_val = max(freq, key=freq.get)
            ans.append(max_val)
            freq.pop(max_val)
        
        return ans