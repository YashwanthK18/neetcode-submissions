class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        for i in nums:
            p*=i
        ans=[]
        for i in range (len(nums)):
            if nums[i]!=0:
                ans.append(int(p/nums[i]))
            else:
                b=nums[:i]+nums[i+1:]
                p1=1
                for j in b:
                    p1*=j
                ans.append(int(p1))
        return ans