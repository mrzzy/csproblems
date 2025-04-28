#
# CSProblems
# Elements of Programming Interviews
# 4.8 Reverse Digits
#

def reverse(n: int) -> int:
    sign, n = n >= 0, abs(n)
    result = 0
    while n > 0:
        # shift place of previous result
        result *= 10
        # extract last digit of current number and add to result
        digit = n % 10
        result += digit
        # remove extracted digit from number
        n //= 10

    return  result if sign else -result

if __name__ == '__main__':
    print(reverse(-432))
    print(reverse(234))
