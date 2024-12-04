class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for e in arr:
            # print(e)
            # print(e/2)
            has_half = int(e/2) in s and e%2 == 0
            has_double = e*2 in s
            if (has_half or has_double):
                return True
            s.add(e)
        
        # print(s)
        return False