class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l=0
        r=len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                a=(r-l)*heights[l]
                l+=1
            else:
                a=(r-l)*heights[r]
                r-=1
            m=max(m,a)
        return m