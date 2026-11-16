class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in range(2):
            for num in nums:
                list1.append(num)
        return list1