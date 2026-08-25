class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set(nums)
        if len(array)==len(nums):
            return False
        return True