class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        
        #heapify and pop 2 largest
        #find diff (or destroyed if same)
        #push diff
        #repeat
        #do it until there's 1 or no stones left:
        
        heapq.heapify_max(stones)
        print("initial_heap", stones)

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second_largest = heapq.heappop_max(stones)
            
            if largest != second_largest:
                heapq.heappush_max(stones, (largest - second_largest))

            #print("steps", stones)

        return stones[0] if stones else 0