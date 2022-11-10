class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0:
            return  str(n // d)
        
        sign = '' if n * d >= 0 else '-'
        n, d = abs(n), abs(d)
        res = sign + str(n // d) + '.'
        n %= d
        i, part = 0, ''
        map = {n : i}
        
        while n % d:
            n *= 10
            i += 1
            
            rem = n % d
            part += str(n // d)
            if rem in map:
                part = part[:map[rem]] + '('+ part[map[rem]:] +')'
                return res + part
            
            map[rem] = i
            n = rem
        return res + part
            
