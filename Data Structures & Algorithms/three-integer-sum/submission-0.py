class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set() 
        for i in range(len(nums)):
            t = -nums[i]
            d = defaultdict(int)
            for j in nums[i + 1:]:
                if t-j in d: 
                    ans.add(tuple(sorted([nums[i], j, t - j]))) 
                d[j] += 1 
        return [list(triplet) for triplet in ans]
