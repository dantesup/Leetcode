class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return 0
        high=len(height)-1
        low=0
        area=0
        while high!=low:
            area=max((high-low)*min(height[low],height[high]),area)
            if height[high]>=height[low]:
                low+=1
            else:
                high-=1
        return area
if __name__=="__main__":
    s=Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))