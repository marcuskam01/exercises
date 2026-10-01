class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            key_word = frozenset(Counter(word).items())
            if key_word not in d: #if not in d: create new list
                d[key_word] = [word]
                #if in d: append
            else:
                d[key_word].append(word)

        #build hashmap
        #use counter and convert to something hashable as key
        #words are values
        #unpack dict and group

        return list(d.values())