/*
 * CSProblems
 * Leetcode
 * 125. Valid Palindrome
 */

package leetcode;

import java.util.function.Function;
import java.util.stream.Stream;

public class Solution {
    public boolean isPalindrome(String s) {
        // strip no-alphanumeric & convert to lowercase
        s = String.join("", s.chars().boxed()
                .flatMap(new Function<Integer, Stream<Character>>() {
                    @Override
                    public Stream<Character> apply(Integer t) {
                        return (Character.isLetterOrDigit(t)) ? Stream.of((char) t.intValue()) : Stream.of();
                    }
                })
                .map(c -> String.valueOf(c))
                .toList())
                .toLowerCase();

        // use two pointers moving from either end of the string
        for (int i = 0; i < s.length() / 2; i++) {
            int j = s.length() - i - 1;
            // verify palindrome property
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
