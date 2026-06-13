class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i, num in enumerate(nums):
            if target-num in dict_num:
                return [dict_num[target-num], i]
            dict_num[num] = i
        return -1