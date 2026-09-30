class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append([i, height])
                area = i*height
            else:
                index = i
                while stack and height <= stack[-1][1]:
                    a = stack.pop()
                    max_area = max(max_area, (i-a[0])*a[1])
                    index = a[0]

                stack.append([index, height])


        return max([max(max_area, h*(len(heights) - i)) for i, h in stack])