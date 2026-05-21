class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()

                b = int(b)
                a = int(a)

                if token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
                elif token == "+":
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)

        ans = stack.pop()
        return int(ans)