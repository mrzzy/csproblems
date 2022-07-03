package leetcode.threesum;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

/** Leetcode 15 3sum Solution */
class Solution {
  /**
   * Finds 3 sized lists of integers (i, j, k) where i + j + k = 0.
   *
   * <p>Integers i, j, k (known as 3sum) are sampled from the given list of integers {@code nums}.
   * Only generates unique lists of i, j, k ie if i, j, k is generated, k, j, i will not be included
   * even though it satisfies the 3 sum criteria.
   *
   * @param nums an array of integers to sample 3 sum from.
   * @return List of 3 sizes lists (i, j, k) representing the 3 sums found.
   */
  public List<List<Integer>> threeSum(int[] nums) {
    // check that we have enough int to generate 3 sums
    if (nums.length < 3) {
      return new LinkedList<>();
    }

    Set<List<Integer>> threeSums = new HashSet<>();

    // precompute a reverse index for O(1) lookup of index k of num[k] in the set
    HashMap<Integer, Integer> reverseNums = new HashMap<>(nums.length);
    for (int i = 0; i < nums.length; i++) {
      reverseNums.put(nums[i], i);
    }

    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        // since nums[i] + nums[j] + nums[k] = 0 is equivalent to nums[i] + nums[j] = -nums[k]
        // we can compute expected num[k] from nums[i], nums[j] in nums[k] = -(nums[i] + nums[j])
        int expectedNumK = -(nums[i] + nums[j]);

        // double check that expected k actually exists in given nums
        if (!reverseNums.containsKey(expectedNumK)) {
          continue;
        }

        // filter out duplicates
        int k = reverseNums.get(expectedNumK);
        if (i == k || j == k) {
          continue;
        }

        // construct a 3 sum triple, sorted to identity duplicates in set.
        List<Integer> triple = Arrays.asList(nums[i], nums[j], nums[k]);
        triple.sort(Comparator.naturalOrder());
        threeSums.add(triple);
      }
    }

    return new LinkedList<>(threeSums);
  }
}
