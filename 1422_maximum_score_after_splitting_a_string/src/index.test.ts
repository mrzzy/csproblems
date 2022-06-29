/*
 * Leetcode
 * 1422. Maximum Score After Splitting a String
 * Unit Tests
*/

const solution = require("./index");

test("score(): tallys left, right scores.", () => {
    expect(solution.score("00", 1)).toStrictEqual([1, 0]);
    expect(solution.score("10", 1)).toStrictEqual([0, 0]);
    expect(solution.score("01", 1)).toStrictEqual([1, 1]);
    expect(solution.score("11", 1)).toStrictEqual([0, 1]);

    expect(solution.score("011010", 3)).toStrictEqual([1, 1]);
    expect(solution.score("100101", 3)).toStrictEqual([2, 2]);
});
