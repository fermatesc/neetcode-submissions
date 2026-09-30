class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx1=0
        idx2=len(heights)-1
        max_area =(idx2-idx1)*min(heights[idx1], heights[idx2])
        while idx1<idx2:
            area=(idx2-idx1)*min(heights[idx1], heights[idx2])
            if area < max_area:
                if  heights[idx1] < heights[idx2]:
                    idx1 += 1
                elif  heights[idx1] > heights[idx2]:
                    idx2 -= 1
                else:
                    idx1 += 1
            if area >= max_area:
                max_area = area
                if  heights[idx1] < heights[idx2]:
                    idx1 += 1
                elif  heights[idx1] > heights[idx2]:
                    idx2 -= 1
                else:
                    idx1 += 1

        return max_area