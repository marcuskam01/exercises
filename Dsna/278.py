class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n 
        mid = 1
        while low <= high:
            mid = (high + low) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            
            elif (isBadVersion(mid-1) == False and isBadVersion(mid)) == True:
                return mid

            else:
                high = mid - 1
        
        return mid