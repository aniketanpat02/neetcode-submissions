class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        height = 0
        while left < right: 
            c_height =min(heights[left], heights[right]) * (right - left)
            if c_height > height:
                height = c_height

            if heights[left] < heights[right]: 
                left+=1
            elif heights[left] > heights[right]:
                right -=1
            elif heights[left] == heights[right]:
                left+=1
                right -=1

        return height