/*
 * Leetcode
 * 1422. Maximum Score After Splitting a String
 */

/* Compute the [left, right] score given the string & cut position. */
function score(s: string, cut: number): [number, number] {
  let [left, right] = [0, 0];
  Array.from(s).forEach((c, idx) => {
    // check if c adds the left or right substring
    const belongsTo = idx < cut ? "left" : "right";

    // update left / right score if c stastfies their criteria
    if (belongsTo == "left" && c == "0") {
      left += 1;
    }
    if (belongsTo == "right" && c == "1") {
      right += 1;
    }
  });

  return [left, right];
}

/* Compute & return max score after splitting a string according to 1422. rules. */
function maxScore(s: string): number {
  // warm up cache of left, right scores
  // compute score cutting string at position 1
  let [left, right] = score(s, 1);

  // move cut position across string, updating left, right score caches
  let max = left + right;
  for (let cut = 2; cut < s.length; cut++) {
    if (s.at(cut - 1) == "0") {
      // left substr gained a '0' char
      left += 1;
    }
    if (s.at(cut - 1) == "1") {
      // right substr lost a '1' char
      right -= 1;
    }

    // keep the max left + right score as max score
    max = Math.max(left + right, max);
  }

  return max;
}

module.exports.score = score;
module.exports.maxScore = maxScore;
