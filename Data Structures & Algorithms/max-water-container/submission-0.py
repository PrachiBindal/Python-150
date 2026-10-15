class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        left_maxi=0
        left_maxi_index=0
        right_maxi=0
        right_maxi_index=j
        ans=0
        while i<j:
            if left_maxi<heights[i]:
                left_maxi=heights[i]
                left_maxi_index=i
            if right_maxi<heights[j]:
                right_maxi=heights[j]
                right_maxi_index=j
        
            ans=max(ans,(min(left_maxi,right_maxi)*(right_maxi_index-left_maxi_index)))
            if left_maxi<right_maxi:
                i+=1
            else:
                j-=1
        return ans


        