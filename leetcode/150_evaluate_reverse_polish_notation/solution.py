#
# CS Problems
# Leetcode
# 150. Evaluate Reverse Polish Notation
#


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            # just 1 value, no operators
            return int(tokens[0])

        stack = []
        for token in tokens:
            # token is an operator: perform operation & push the result onto stack
            if token == "+":
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)
            elif token == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif token == "/":
                # int() discards decimal portion of devision result, rounding towards 0.
                # floor division is NOT used here as it always rounds down,
                # leading to undesirable round down when quotient is negative.
                right, left = stack.pop(), stack.pop()
                stack.append(int(left / right))
            elif token == "*":
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)

            # token is an operand, push it onto the stack
            else:
                stack.append(int(token))

        # last value on the stack is the result of evalution
        return stack[-1]
