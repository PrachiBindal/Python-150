class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we will use map for this
        # the map will store whether it was already there or not, and if not then we can
        mpp={}
        ans=0
        j=-1
        for i in range(len(s)):
            if s[i] in mpp and mpp[s[i]]>j:
                j=mpp[s[i]]
            mpp[s[i]]=i
            ans=max(ans,(i-j))
        return ans