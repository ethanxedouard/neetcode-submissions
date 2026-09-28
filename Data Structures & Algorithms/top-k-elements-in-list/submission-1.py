class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        mostFreq = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for i in range(k):
            x = max(freq, key=freq.get)
            mostFreq.append(x)
            freq.pop(x)
        
        return mostFreq