#include <string>

using namespace std;

class Solution {
public:
  string expandPalindrome(string s, int left, int right) {
    if (left > right) {
      // overlapping interval cannot be expanded
      throw "Overlapping bounds";
    }

    // expand palindrome bounds until palindrome property is violated
    while (left > 0 && right < s.size() - 1) {
      if (s[left - 1] != s[right + 1]) {
        break;
      }
      left--;
      right++;
    }

    int length = right - left + 1;
    return s.substr(left, length);
  }

  string longestPalindrome(string s) {
    string longest = "";
    for (int i = 0; i < s.size(); i++) {
      // establish bounds of the palindromic substring
      int left = i;
      int right = i; // inclusive
      // odd palindromic string
      string palindrome = expandPalindrome(s, left, right);
      if (palindrome.size() > longest.size()) {
        longest = palindrome;
      }

      if (i > 0 && s[i - 1] == s[i]) {
        // even palindromic string
        left = i - 1;
        string palindrome = expandPalindrome(s, left, right);
        if (palindrome.size() > longest.size()) {
          longest = palindrome;
        }
      }
    }
    return longest;
  }
};
