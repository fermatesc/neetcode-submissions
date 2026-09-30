class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers)-1
        while True:
            sum = numbers[idx1]+numbers[idx2]
            if sum == target:
                return [idx1+1, idx2+1]
            elif sum < target:
                idx1 += 1
            else:
                idx2 -= 1