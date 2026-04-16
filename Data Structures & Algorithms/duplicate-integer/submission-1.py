class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       dupcheck = set()
       for i,num in enumerate(nums):
        if num not in dupcheck:
            dupcheck.add(num)
        else:
            return True
       return False
        




        