/*
 * Cracking the coding interview
 * Chapter 1 2. Check Permutations.
 */

#include <cassert>
#include <memory>
#include <string>
#include <unordered_map>

/*
 * Counts the number of each unique character appears in given strings
 * Returns a unique_ptr to a map of character to no. of appearances.
 */
std::unique_ptr<std::unordered_map<char, uint32_t>> countChars(
    const std::string& str) {
  auto charCounts = std::make_unique<std::unordered_map<char, uint32_t>>();

  for (auto c : str) {
    // try to get count for char or default to 0
    auto countOptional = charCounts->find(c);
    uint32_t charCount =
        (countOptional != charCounts->end()) ? countOptional->first : 0;
    // update char count to reflect character
    (*charCounts)[c] = charCount + 1;
  }

  return charCounts;
}

/*
 * Checks if the given strings are permutations of each other.
 * Returns true if strings are permutations of each other, false otherwise.
 */
bool checkPermutation(const std::string& leftStr, const std::string& rightStr) {
  // check for special cases
  // sizes don't line up: strings cannot be permutations of each other
  if (leftStr.size() != rightStr.size()) {
    return false;
  }
  // if strings are identical, they are permutations of each
  if (leftStr == rightStr) {
    return true;
  }

  // count the no. of appearances of chars in strings
  auto leftCharCounts = countChars(leftStr);
  auto rightCharCounts = countChars(rightStr);

  // for every character c in leftStr, check that the same character c
  // exists in rightStr with an equal no. of appearances
  for (auto leftCharCount : *leftCharCounts) {
    auto rightCharCountOptional = rightCharCounts->find(leftCharCount.first);
    uint32_t rightCount = (rightCharCountOptional != rightCharCounts->end())
                              ? rightCharCountOptional->second
                              : 0;

    // check no. of appearances on the left string matches up with the right
    // string
    if (rightCount != leftCharCount.second) {
      return false;
    }
  }

  // since all char appearances match up, left and right strings must be
  // permutations of each other
  return true;
}

int main() {
  // test special cases
  assert(checkPermutation("", ""));
  assert(checkPermutation("abc", "abc"));
  assert(!checkPermutation("asdf", "sdf"));
  assert(!checkPermutation("gg", "gggg"));

  // test example cases
  assert(checkPermutation("abcde", "eadcb"));
  assert(checkPermutation("asdggf", "gfdsag"));
  assert(!checkPermutation("bcde", "wxyz"));
}
