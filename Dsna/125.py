class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        #check left and right indices
        #if same then shrink the pointers
        #else return false

        #implementation:
        #start at 0, end
        #check if theyre alphabets
        #if they are, check if theyre the same
        #if not instant return false
        #if one of them is not an alphabet, advance (left+1 or right-1)
        #check again until it is an alphabet
        #if theyre different alphabets, return false
        #continue until l=r or l=r-1
        #return true
        while l < r:
            #cond 1: both are alnum, compare, move both pointers
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False

            #cond 2: l isn't, move l
            elif not s[l].isalnum():
                l += 1
            #cond 3: r isn't, move r
            elif not s[r].isalnum():
                r -= 1

        return True
