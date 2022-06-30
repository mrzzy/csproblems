/*
 * Leetcode
 * 1422. Maximum Score After Splitting a String
 * Unit Tests
 */

const sol = require("./index");

test("score(): tallys left, right scores.", () => {
  expect(sol.score("00", 1)).toStrictEqual([1, 0]);
  expect(sol.score("10", 1)).toStrictEqual([0, 0]);
  expect(sol.score("01", 1)).toStrictEqual([1, 1]);
  expect(sol.score("11", 1)).toStrictEqual([0, 1]);

  expect(sol.score("011010", 3)).toStrictEqual([1, 1]);
  expect(sol.score("100101", 3)).toStrictEqual([2, 2]);
});

test("maxScore(): find the max score attainable in 2 substrs.", () => {
  expect(sol.maxScore("00")).toBe(1);
  expect(sol.maxScore("011101")).toBe(5);

  // verify correctness of larger test cases with brute force
  const maxScoreBrute = (s: string): number =>
    Array.from(s)
      .map((_, cut) =>
        cut < 1 || cut >= s.length ? [0, 0] : sol.score(s, cut)
      )
      .map(([left, right]) => left + right)
      .reduce((first, second) => Math.max(first, second));

  const cases = [
    "11010101010101111111",
    "11111111111111111111",
    "00000000000000000000",
    "10101000111001010010",
  ];
  for (const c of cases) {
    console.log(c);
    expect(sol.maxScore(c)).toBe(maxScoreBrute(c));
  }
});
