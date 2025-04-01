#
# CSProblems
# Elements of Programming Interviews
# 4.7 Compute x**y
#

def pow(x: int, y: int) -> int:
    if y < 0:
        raise ValueError("Cannot compute power of x: y < 0")

    # iteratively compute x**y
    result = 1
    while y > 0:
        if y % 2 == 1:
            # y is odd
            y -= 1
            result *= x
        else:
            # y is even: apply squaring to speed up power computation
            y /= 2
            result *= result

    return result


if __name__ == '__main__':
    print(pow(2, 9))
