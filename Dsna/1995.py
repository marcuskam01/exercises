class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        #brute force is O(n^4)
        #according to tips 1&2
        #can be optimised to O(n^2) by using a hashmap to store the sums of pairs and then checking for the 4th number
        #will be completed in the future
        sol_count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k] == nums[l]:
                            sol_count += 1
        return sol_count