class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,col=len(matrix),len(matrix[0])
        first,last=0,rows-1
        while first<=last:
            mid = (first+last)//2
            if target<matrix[mid][0]:
                last = mid - 1
            elif target > matrix[mid][-1]:
                first=mid+1
            else:
                break
        if not (first<=last):
            return False
        row = (first+last)//2
        l,r = 0,col-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l= m+1
            elif target < matrix[row][m]:
                r=m-1
            else:
                return True
        return False


        