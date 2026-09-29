class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l = 0
        r = len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                trapped += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                trapped += maxRight - height[r]
        
        return trapped
