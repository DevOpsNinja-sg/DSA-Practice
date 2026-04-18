class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        mid = len(nums)//2

        leftarray = nums[:mid]
        rightarray = nums[mid:]

        sortleft = self.sortArray(leftarray)
        sortright = self.sortArray(rightarray)


        return self.merge(sortleft,sortright)

    def merge(self,leftarray,rightarray):
        result = []
        i=j=0

        while i <len(leftarray) and j<len(rightarray):
            if leftarray[i]<rightarray[j]:
                result.append(leftarray[i])
                i+=1
            else:
                result.append(rightarray[j])
                j+=1

        result.extend(leftarray[i:])
        result.extend(rightarray[j:])
        return result
            