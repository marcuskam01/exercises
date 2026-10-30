class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window and counter
        #check for freq array in s2 in slices of s1

        #freq array approach, faster
        freq_array = [0] * 26

        for c in s1:
            idx = ord(c) - ord('a')
            freq_array[idx] += 1

        freq_array_substring = [0] * 26

        i = 0
        while i < len(s1) and i < len(s2):
            idx = ord(s2[i]) - ord('a')
            freq_array_substring[idx] += 1
            i += 1

        if freq_array == freq_array_substring:
            return True

        for w in range(len(s1),len(s2)):
            #w give latest letter
            
            #update add new char
            idx = ord(s2[w]) - ord('a')
            freq_array_substring[idx] += 1

            #update remove old char
            idx = ord(s2[w-len(s1)]) - ord('a')
            freq_array_substring[idx] -= 1

            #compare
            if freq_array == freq_array_substring:
                return True
        
        return False

        #Counter approach, slower
        # s1c = Counter(s1)
        # for w in range(len(s2)-len(s1)+1):
        #     #print(s2[w:w+len(s1)])
        #     wc = Counter(s2[w:w+len(s1)])
        #     if s1c == wc:
        #         return True
        
        # return False