class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            point = (left + right)// 2
            if nums[point] > target:
                right = point - 1
            elif nums[point] < target:
                left = point + 1
            else:
                return point
        return -1
        
                