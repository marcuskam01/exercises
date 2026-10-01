from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode with length of string and delimiter
        s = ""
        for word in strs:
            s = s+str(len(word))+"-"+word
        return s

    def decode(self, s: str) -> List[str]:
        pos = 0
        l = []

        while pos < len(s):
            #find delimiter
            ind = s.index("-",pos)
            #read length of string
            length_of_segment = s[pos:ind]
            #use the value of length to read the string and append to list
            l.append(s[pos+len(length_of_segment)+1:pos+len(length_of_segment)+1+int(length_of_segment)])
            #skip over the length of string and delimiter to the next word
            pos += len(length_of_segment) + 1 + int(length_of_segment)

        return l
