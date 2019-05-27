#!/usr/bin/env python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len1 = len(nums)
        for i in range(len1):
            a = target - nums[i]
            if a in nums:
                if nums.index(a) != i:
                    return [i,nums.index(a)]