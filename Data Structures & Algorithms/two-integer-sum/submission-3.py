class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nam = {}

        for i in range(len(nums)):
            nam[nums[i]] = i

        for i in range(len(nums)):
            find = target - nums[i]

            if find in nam and nam[find] != i:
                return [i, nam[find]]
        
        return []
        