class Solution:
    def canJump(self, nums: list[int]) -> bool:
        #at each index calculate possible steps from each reachable index
        #index 0: 1 or 2
        #index 1: 2 or 3 or 4
        #index 2: 3
        #if at anypoint it can reach len(nums) return true else false
        i = 0
        farthest = 0
        while i < len(nums):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
            i += 1
            if farthest >= len(nums) - 1:
                return True
        return False