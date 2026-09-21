class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sety=set(nums)

        if len(nums)==len(sety):
            return False
        return True
            
        
        