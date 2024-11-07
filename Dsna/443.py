class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        write = 0
        l = 0

        while l < len(chars):
            char = chars[l]
            r = l
            length = 0

            while r < len(chars) and chars[r] == char:
                r += 1
                length += 1
                chars[write] = char
            write += 1

            if length > 1:
                for num in str(length):
                    chars[write] = num
                    write += 1

            l = r
        return write