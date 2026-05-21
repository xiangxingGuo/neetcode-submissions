class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        cur_area = (right - left) * min(heights[right], heights[left])

        while left < right:
            left_value = heights[left]
            right_value = heights[right]

            if left_value < right_value:
                left += 1
            else:
                right -= 1

            left_value = heights[left]
            right_value = heights[right]
            temp_area = (right - left) * min(left_value, right_value)

            cur_area = max(cur_area, temp_area)
        
        return cur_area
                


        