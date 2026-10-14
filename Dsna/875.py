class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #min speed: 1
        #max speed: max(piles)
        #find condition in which sum(math.ceil(piles[i]/ k)) <= h 
        l, r = 1, max(piles)
        ans = r 
        while l <= r:
            mid = (l+r) // 2
            #sum > h: too slow, increase l
            if sum(math.ceil(p / mid) for p in piles) > h:
                l = mid + 1
            #sum < h: too fast, decrease r but keep the min sol
            elif sum(math.ceil(p / mid) for p in piles) <= h:
                ans = mid
                r = mid - 1
        return ans