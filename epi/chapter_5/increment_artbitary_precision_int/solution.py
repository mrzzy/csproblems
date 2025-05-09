#
# CSProblems
# Elements of Programming Interviews
# 5.2 Increment Arbitrary Precision Integer
#


def increment(digits: list[int]):
    # init carry to 1 to increment first digit
    carry = 1
    # perform sum digit by digit using carry
    for i in range(len(digits) - 1, -1, -1):
        sum_ = digits[i] + carry
        digits[i] = sum_ % 10
        carry = sum_ // 10

    # add digit for carry if still present
    if carry != 0:
        digits.insert(0, carry)

    return digits


if __name__ == "__main__":
    print(increment([9, 9, 9, 9, 9]))
    print(increment([1, 2, 3]))
    print(increment([0]))
    print(increment([1]))
    print(increment([0, 0, 0, 0, 0]))
    print(increment([1, 2]))
