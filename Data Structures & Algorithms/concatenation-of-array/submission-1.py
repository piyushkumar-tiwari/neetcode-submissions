class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = []
        x = len(nums)
        list1 = [0] * (2*x)
        for i, num in enumerate(nums):
            list1[i] = list1[x+i] = num
        return list1