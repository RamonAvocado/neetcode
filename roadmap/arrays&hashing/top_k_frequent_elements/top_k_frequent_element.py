class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_set = set(nums)
        best_numbers = []
        for num in nums_set:
            best_numbers.append((nums.count(num), num))
        
        best_numbers.sort(key=lambda x: x[0])
        return [num[1] for num in best_numbers[-k:]]

