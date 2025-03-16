#
# CSProblems
# Elements of Programming Interviews
# 5.6 Buy & Sell Stock Once
#


def max_profit(prices: list[int]):
    if len(prices) <= 1:
        return 0

    profit = 0
    max_price = prices[len(prices) - 1]
    for i in range(len(prices) - 2, -1, -1):
        profit = max(profit, max_price - prices[i])
        max_price = max(max_price, prices[i])

    return profit


if __name__ == "__main__":
    print(max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
