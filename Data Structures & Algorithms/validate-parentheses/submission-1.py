class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if pairs[char] != top:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False