class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        max_val = len(grid[0])**2
        count = {}
        for row in grid:
            for val in row:
                count[val] = count.get(val, 0) + 1
        
        for value in range(1, max_val+1):    
            if count.get(value, 0) == 2:
                a = value
            elif count.get(value, 0) == 0:
                b = value

        return [a, b]
        