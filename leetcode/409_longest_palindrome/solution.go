/*
 * CSProblems
 * Leetcode
 * 409. Longest Palindrome
*/
 
package main

func longestPalindrome(s string) int {
    // count no. of pairs and singles
    nPairs := 0
    singles := make(map[rune]bool)
    for _, c := range s {
        if _, ok := singles[c]; ok  {
            nPairs += 1
            delete(singles, c)
        } else {
            singles[c] = true
        }
    }

    // calculate size of longest palindrome:
    // - 2* no. of pairs
    // - +1 if any singles are present
    if len(singles) > 0 {
        return 2 * nPairs + 1
    } else {
        return 2 * nPairs + 0
    }
}
