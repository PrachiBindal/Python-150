class Solution:
    def twoSum(self, i:int, nums: List[int], target: int) -> List[int]:
        j=len(nums)-1
        ans=[]
        while i<j:
            if nums[i]+nums[j]==target:
                ans.append([nums[i], nums[j]])
                i+=1
                j-=1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
        return ans
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for k in range(0,len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                continue
            Solve=self.twoSum(k+1, nums,-nums[k])
            for pair in Solve:
                ans.append([nums[k]]+pair)
        return ans
        