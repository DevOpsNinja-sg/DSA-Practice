class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res={}

        for i,num in enumerate(numbers):
            complement=target-num
            if complement in res:
                return [res[complement]+1,i+1]
            res[num]=i