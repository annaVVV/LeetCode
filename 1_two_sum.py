# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 10000 <= len(nums) <= 2: return  "Invalid list lenth" 
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i] 
            dif = target - num
            d[dif] = i
        return []
