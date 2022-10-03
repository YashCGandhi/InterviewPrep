def decodeString(self, s: str) -> str:
        stack = []
        curStr, curNum = '',0
        for i in s:
            
            if i == '[':
                stack.append(curStr)
                stack.append(curNum)
                curStr = ''
                curNum = 0
            elif i ==']':
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + num*curStr
                
            elif i.isdigit():
                print(i)
                # because the number given is also a string and is read digit by digit
                curNum = curNum*10 + int(i)
            else:
                curStr += i
        return curStr
       
        
