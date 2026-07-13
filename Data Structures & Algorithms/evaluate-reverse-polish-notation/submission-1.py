class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ("+", "-", "*", "/"):
                num_1 = stack.pop()
                num_2 = stack.pop()
                if token == "+":
                    result = num_1 + num_2
                if token == "-":
                    result = num_2 - num_1
                if token == "*":
                    result = num_1 * num_2
                if token == "/":
                    result = int(num_2 / num_1)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]
                                                                        