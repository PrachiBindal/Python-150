class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        ans=0
        n=len(prices)
        for i in range(n-1,-1,-1):
            ans=max(ans,max(0,maxi-prices[i]))
            maxi=max(maxi,prices[i])
        return ans
                

        