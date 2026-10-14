class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #// operator rounds down
        #finds mid, compare mid to nums, move left or right accordingly and avoid infinite loop
        #if found return mid, if not found return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            #overshoot:
            if nums[mid] > target:
                r = mid - 1
            #undershoot
            elif nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] == target:
                return mid

        return -1