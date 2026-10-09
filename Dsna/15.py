class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #sort first, n log n
        nums.sort()
        #walk through the list using 1 pointer as anchor, implement 2sum while the 3rd sum is fixed
        sol = []
        for i in range(len(nums)):
            #cant get 0 if theyre all positive
            if nums[i] > 0:
                break
            #-nums[i] is how much you need the other 2 to add up to, aka target
            #skip over if the prev one is the same
            if i != 0 and nums[i-1] == nums[i]:
                continue
            #check for new val
            l, r = i+1, len(nums)-1
            #once found, append nums[i] nums[l] and nums[r]
            while l < r:
                #if too small
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                #if too big
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                #only append if they add up to 0
                elif nums[l] + nums[r] == -nums[i]:
                    sol.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    #skip over pointers of repeated values
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
        return(sol)