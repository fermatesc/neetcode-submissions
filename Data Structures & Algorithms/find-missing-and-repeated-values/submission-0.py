class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        max_val = len(grid[0])**2
        grid = sum(grid, [])
        seen = {}
        for val in grid:
            if val not in seen:
                seen[val] = 1
            else:
                a = val
                break

        for i in range(1, max_val+1):
            if i not in grid:
                b = i
                break    

        return [a, b]
        