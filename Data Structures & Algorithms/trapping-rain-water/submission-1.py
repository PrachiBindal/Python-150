class Solution:
    def trap(self, height: List[int]) -> int:

        # approach 1:
        # for every index, it is min(left_maxi, right_maxi)-height[i]
        left_maxi=0
        right_maxi=0
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        
        for i in range(0,n):
            # print(i)
            prefix[i]=left_maxi
            suffix[n-1-i]=right_maxi
            left_maxi=max(left_maxi,height[i])
            right_maxi=max(right_maxi,height[n-1-i])
            # print(f"prefix[i]:{prefix[i]}")
            # print(f"suffix[n-1-i]:{suffix[n-1-i]}")
        ans=0
        for i in range(1,n-1):
            x=min(prefix[i],suffix[i])-height[i]
            ans=ans+max(0,x)
        return ans

        # approach 2 we can divide this in three parts 
        # find greatest 2
        # and then go left and there righnt

        # start=height[0]
        # i=0
        # set(height.begin(),hei)
        # while i<len(height):

        