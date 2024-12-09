class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        curr = 1
        max_val = 1

        for e in s:
            if (e-1) not in s: #start of array
                start = e
                curr = 1
                while (start+1) in s:
                    start += 1
                    curr += 1
                max_val = max(max_val, curr)
        
        return max_val

        