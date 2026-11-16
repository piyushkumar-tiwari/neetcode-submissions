class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in number:
                return [number[complement], i]
            number[num] = i
                