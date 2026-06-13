class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        mockDict = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c in mockDict:
                if x and x[-1] == mockDict[c]:
                    x.pop()
                else:
                    return False
            
            else:
                x.append(c)

        return True if not x else False


            

