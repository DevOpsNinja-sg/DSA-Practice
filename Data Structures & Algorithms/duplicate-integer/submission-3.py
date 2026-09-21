class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res={}

        for num in nums:
            res[num] = res.get(num,0)+1

        for key,val in res.items():
            if val>1:
                return True
        return False
            
        
        