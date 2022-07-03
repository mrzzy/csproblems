/*
 * Cracking the Coding Interview
 * Chapter 1
 * String Compression solution test
 */

const { tabulate, compress } = require("./compress.js");

test("tabulate() tabulation of run counts", () => {
  expect(tabulate("")).toEqual([]);
  expect(tabulate("a")).toEqual([["a", 1]]);
  expect(tabulate("abb")).toEqual([
    ["a", 1],
    ["b", 2],
  ]);
  expect(tabulate("aabbbbcccccc")).toEqual([
    ["a", 2],
    ["b", 4],
    ["c", 6],
  ]);
  expect(tabulate("aabaaa")).toEqual([
    ["a", 2],
    ["b", 1],
    ["a", 3],
  ]);
});

test("compress() compresses long strings with character run compression", () => {
  expect(compress("aabbbbcccccc")).toEqual("a2b4c6");
  expect(compress("aaabbbba")).toEqual("a3b4a1");
  expect(compress("aabbbccccdddd")).toEqual("a2b3c4d4");
  expect(compress("asdf")).toEqual("asdf");
  expect(compress("a")).toEqual("a");
  expect(compress("")).toEqual("");
});
