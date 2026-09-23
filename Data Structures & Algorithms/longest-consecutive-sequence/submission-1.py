class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mpp={}
        nums=sorted(nums)
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            if num in mpp:
                if num+1 in mpp:
                    mpp[num]=max(mpp[num],mpp[num+1]+1)
            else:
                if num+1 in mpp:
                    mpp[num]=mpp[num+1]+1
                else:
                    mpp[num]=1
        ans=1
        for ele, length in mpp.items():
            ans=max(ans,length)
        return ans
        