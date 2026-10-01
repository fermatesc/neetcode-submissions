class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        state = []
        l = 0
        window = {}
        for r in range(0, len(nums)):
            if nums[r] in window and (r - window[nums[r]]) <= k:
                return True
            window[nums[r]] = r
        return False