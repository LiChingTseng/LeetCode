class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            if (right-left) * min(height[left], height[right]) > max_area:
                max_area = (right-left) * min(height[left], height[right])
            if height[right] < height[left]:
                right -= 1
            else: 
                left += 1
            
        return max_area
