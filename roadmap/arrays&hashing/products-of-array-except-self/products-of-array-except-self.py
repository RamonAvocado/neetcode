from functools import reduce

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1,2,4,6]
        # [2,4,6]
        # [1,4,6]
        # [1,2,6]
        # [1,2,4]
        result = []
        for i, n in enumerate(nums):
            second_list_split = i-len(nums)+1 
            if second_list_split == 0:
                count_list = nums[:i]
            else:
                count_list = nums[:i] + nums[i-len(nums)+1:]
            
            print(f"i{i}", count_list)
            result.append(reduce(lambda x, y: x*y, count_list))


        return result
