class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area_max = 0
        while i <= j:
            left = heights[i]
            right = heights[j]
            dis = j - i
            area = dis * min(left, right)

            if area > area_max:
                area_max = area
            if left > right:
                j -= 1
            else:
                i += 1
        return area_max