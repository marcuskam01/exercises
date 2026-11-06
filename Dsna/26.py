class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #read and write pointer
        if len(nums) == 1:
            return 1

        j = 1

        for i in range(1,len(nums)):
            #scan for unique numbers
            #the nums[j] = number of unique numbers in nums
            #if i and the previous are not the same, move j until end of array
            if nums[i] != nums[i-1]:
                print(j)
                
                nums[j] = nums[i]
                j += 1

        return j