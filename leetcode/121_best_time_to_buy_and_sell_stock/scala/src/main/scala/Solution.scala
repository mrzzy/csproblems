/*
 * leetcode
 * 121. Best Time to Buy and Sell Stock
 */


object Solution {

  case class StockResult(maxProfit: Int, minPrice: Int)

  /** Computes the max profit that can be gain by buying and selling a stock.
    *
    * Given the stock's prices, determines the best day to buy and sell the
    * stock such that prices[buyDay] - prices[sellDay]ois the max possible.
    *
    * @param prices
    *   Array of stock prices by day.
    * @returns
    *   the max possible profit that can obtained by buying and selling the
    *   stock.
    */
  def maxProfit(prices: Array[Int]): Int = {
    prices.foldLeft(StockResult(0, Int.MaxValue)) {
      case (StockResult(prevProfit, prevMinPrice), price) => {
        val minPrice = Math.min(prevMinPrice, price)
        val profit = Math.max(prevProfit, price - minPrice)
        StockResult(profit, minPrice)
      }
    }.maxProfit
  }
}
