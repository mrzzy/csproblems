/*
 * CSProblems
 * Leetcode
 * 322. Coin Change
*/
function coinChange(coins: number[], amount: number): number {
  // init min coins cache
  const minCoins = Array(amount + 1).fill(Number.MAX_VALUE);
  minCoins[0] = 0;

  // build min coins solution bottom up from base cases
  for (let i = 1; i <= amount; i++) {
    // try each coin and save best solution
    coins.forEach((c) => {
      const remainder = i - c;
      if (
        minCoins[remainder] != null &&
        minCoins[remainder] !== Number.MAX_VALUE
      ) {
        minCoins[i] = Math.min(minCoins[i], minCoins[remainder] + 1);
      }
    });
  }

  return minCoins[amount] == Number.MAX_VALUE ? -1 : minCoins[amount];
}
