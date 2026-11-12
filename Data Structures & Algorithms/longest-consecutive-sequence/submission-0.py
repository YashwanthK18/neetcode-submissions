class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        c=1
        m=c
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]-1:
                c+=1
            else:
                c=1
            if c>m:
                m=c
        return m