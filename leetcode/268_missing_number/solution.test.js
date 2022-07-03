/*
 * Leetcode
 * ???. Problem Name
 * Solution tests
 */

const missingNumber = require("./solution").missingNumber;

test("missingNumber() finds missing number", () => {
  expect(missingNumber([0])).toBe(1);
  expect(missingNumber([0, 1])).toBe(2);
  expect(missingNumber([3, 0, 1])).toBe(2);
  expect(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])).toBe(8);
});
