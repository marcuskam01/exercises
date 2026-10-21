class Solution:
    def findMin(self, nums: list[int]) -> int:
        #instead of searching for target
        #search for boundary (where rotation began)
        #if mid > nums[r]: boundary to the right
        #if mid < nums[r]: boundary to the left
        l, r = 0, len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        #[6,-1,0,1,3]
        #mid=2, nums[mid] = 0
        #0<3, boundary to the left
        #r = 2
        #mid = 1, nums[mid] = -1
        #-1<3, boundary to the left but then -1 is the min
        #r = 1
        #mid = 0
        #l = 1
        #loop quit, returns 6 which is incorrect, return pointer location instead

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            #all elements are unique no need for mid == nums[r]
        return nums[l] 