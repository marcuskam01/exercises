class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        #can't finish if cost > gas
        if sum(gas) - sum(cost) < 0:
            return -1

        # gas[i] - cost[i] + gas[i+1]
        #curr_gas += gas[i] - cost[i]

        curr_gas = 0
        start = 0

        #eliminate possibilities given 1 unique solution
        #if curr_gas goes negative your car cant move

        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0 
            
        return start
        