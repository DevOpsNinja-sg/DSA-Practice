class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        left_max,rit_max=0,0
        water_level=0

        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    left_max = height[left]
                else:
                    water_level+=left_max-height[left]
                left+=1
            else:
                if height[right]>=rit_max:
                    rit_max=height[right]
                else:
                    water_level+=rit_max-height[right]
                right-=1
        return water_level