/*
 * Cracking the Coding Interview
 * Chapter 1
 * String Compression
 */

/**
 * Tabulate the run counts of each character in given string input.
 *
 * A run is defined as a contiguous series of the same character in the string.
 *
 * @param {string} input The input string to tabulate run counts on.
 * @returns {array} array of Array[string,number] defining mappings of character
 *  to run counts.
 */
function tabulate(input) {
  // tabulate run counts for each character
  // list of mappings of character -> run counts
  const runCounts = [];
  let runCount = 0;
  let currentChar = "";
  for (i = 0; i < input.length; i++) {
    if (currentChar != input[i]) {
      // different char:
      // push runCount of previous char into run counts
      if (runCount > 0) {
        runCounts.push([currentChar, runCount]);
      }

      // transition to tracking run counts for new char
      currentChar = input[i];
      runCount = 1;
      continue;
    }

    // same char: increment runcount
    runCount++;
  }
  // push the last run count for the last character
  if (runCount > 0) {
    runCounts.push([currentChar, runCount]);
  }

  return runCounts;
}

/**
 * Compresses the given stringn character run compression.
 *
 * Character run compression compresses strings by shortening successive
 * character runs: (ie 'aaaaabbb' -> 'a5b3'). If the compressed string is longer
 * than the original string, returns the original string instead.
 *
 * @param {string} input input string to compress.
 * @returns {string} the compressed string or the original string if compression
 *  produces a string longer than the original string.
 */
function compress(input) {
  const runCounts = tabulate(input);

  // build compressed string by joining chars with their run lengths.
  const compressed = runCounts
    .map((charCount) => {
      const [char, count] = charCount;
      return char + count;
    })
    .join("");

  return input.length < compressed.length ? input : compressed;
}

exports.tabulate = tabulate;
exports.compress = compress;
