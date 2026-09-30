class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for num in nums:
            if num in groups:
                groups[num]+=1
            else:
                groups[num]=1

        out = sorted(groups, key=lambda x:groups[x])

        return out[-k:]