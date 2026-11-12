class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]-=1
        ans=sorted(d.keys(),key=lambda x: d[x])
        return ans[:k]