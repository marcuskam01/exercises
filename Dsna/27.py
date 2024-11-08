class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                nums.append(nums.pop(i))
                k -= 1
            else:
                i += 1
        return k