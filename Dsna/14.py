class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = list(strs[0])
        if len(strs) == 1:
            return strs[0]
        num_chars = len(chars) 
        sol = ""
        for letter_pos in range(num_chars):
            
            char_verify = set()
            char_verify.add(chars[letter_pos])
            
            for word in strs[1:]:
                if letter_pos < len(word):
                    char_verify.add(word[letter_pos]) 
                else:
                    return sol

            if len(char_verify) == 1:
                sol += chars[letter_pos]
            else: 
                return sol

        return sol