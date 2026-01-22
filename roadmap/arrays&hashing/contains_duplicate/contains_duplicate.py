class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        aux = set()
        for n in nums:
            if n not in aux:
                aux.add(n)
            else:
                return True
        return False
