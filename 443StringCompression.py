class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        i = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j+= 1

            chars[idx] = chars[i]
            idx += 1

            if (j - i > 1):
                cnt = str(j-i)
                for c in cnt:
                    chars[idx] = c
                    idx += 1

            i = j
        return idx 
