/*
 * CSProblems
 * Leetcode
 * 121. Best Time to Buy and Sell Stock
*/

use std::cmp::{max, min};

struct StockState {
    max_profit: i32,
    min_price: i32,
}
impl StockState {
    pub fn new() -> Self {
        Self {
            max_profit: i32::MIN,
            min_price: i32::MAX,
        }
    }
}

struct Solution {}
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // max profit occurs when we buy at min price & sell at max price in that order
        let StockState {
            max_profit,
            min_price: _,
        } = prices.iter().fold(
            StockState::new(),
            |StockState {
                 max_profit,
                 min_price,
             },
             &price| {
                StockState {
                    // update min price seen so far
                    min_price: min(min_price, price),
                    // update max profit seen so far:
                    // - either previous highest profit
                    // - or we buy at min_price and sell at current price.
                    max_profit: max(max_profit, price - min_price),
                }
            },
        );
        // max profit should be above zero
        max(max_profit, 0)
    }
}
pub fn main() {
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
}
