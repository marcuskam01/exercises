class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        #use max heap
        #keep popping the max element until we reach the kth largest
        heapq.heapify_max(nums)
        #print(nums)
        for i in range(k-1):
            heapq.heappop_max(nums)
            #print(nums)
        return nums[0]