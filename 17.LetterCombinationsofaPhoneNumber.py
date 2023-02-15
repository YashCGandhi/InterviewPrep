class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {"2":['a','b','c'],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"], "9":["w","x","y","z"]}
        res = []
        if digits == "":
            return ""
        def backtrack(digit, curStr):
            if digit == "":
                res.append(curStr)
                return
            
            for c in letter_map[digit[0]]:
                curStr += c
                backtrack(digit[1:], curStr)
                curStr = curStr[:-1]
            
        backtrack(digits, "")
        return res

        
