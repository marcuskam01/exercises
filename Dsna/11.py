class Solution:
    def maxArea(self, height: list[int]) -> int:
        #assume full array, initiate l,r
        #vol is length of (r-l) * height of the lower stick
        #store max water
        #move the shorter wall and recalculate water volume
        #if bigger than max water then rewrite max water
        #stop when l meets r
        #if both the same height move either 1
        #return max_water
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            water_vol = min(height[l], height[r]) * (r-l)
            #compare current vol against max
            max_water = max(water_vol, max_water)
            #cond 1: left is shorter, move left
            if height[l] <= height[r]:
                l += 1
            #cond 2: right is shorter, move right
            else:
                r -= 1
        return max_water 