class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in hashmap:
                return [hashmap[j], i]
            else:
                hashmap[nums[i]] = i


