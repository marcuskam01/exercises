class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #[1,3,4,16,18], target 34
        #initiate l,r
        l, r = 0, len(numbers) - 1
        #check l+r.
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return [l+1,r+1]
        #if too big, decrease r
        #if too small, increase l
        #repeat until l+r = target
        #return index of l+1 and index of r+1