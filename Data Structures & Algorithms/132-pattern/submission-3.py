class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s=[]
        x = -math.inf
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<x:
                return True
            while s and nums[i] > s[-1]:
                x = s.pop()
            s.append(nums[i])

        return False
