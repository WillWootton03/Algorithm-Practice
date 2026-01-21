class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        a = 0
        res = 0 
        while l < r:
            sm =  min(height[l], height[r])
            a = (r - l) * sm
            if a > res:
                res = a
            if sm == height[l]:
                l += 1
            elif sm == height[r]:
                r -= 1
        return res