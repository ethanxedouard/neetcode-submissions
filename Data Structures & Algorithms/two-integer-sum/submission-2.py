class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        back = len(nums) - 1

        while back > 0:
            for i in range(back):
                if nums[i] + nums[back] == target:
                    return [i, back]
            back -= 1