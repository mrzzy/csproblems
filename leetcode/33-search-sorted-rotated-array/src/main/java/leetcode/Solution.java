package leetcode;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/** Leetcode 33.Search in Rotated Sorted Array Solution. */
class Solution {

  /** Binary search for the rotation pivot to find rotation offset */
  private static int findRotation(int[] nums, int left, int right) {
    int middle = (right - left) / 2 + left;
    // base case: array is not rotated, so rotation offset must be left
    if (nums[left] <= nums[middle] && nums[middle] < nums[right]) {
      // nums not rotated: rotation offset first element of subarray.
      return left;
    }
    // base case: converged on rotation pivot, hence right should be rotation offset
    if (left == middle) {
      return right;
    }
    // recusively search for rotation pivot in left or right subarrays
    if (nums[left] > nums[middle]) {
      // binary search for rotation pivot in left subarray
      return findRotation(nums, left, middle);
    }
    // binary search for rotation pivot in right subarray
    return findRotation(nums, middle, right);
  }

  /** Binary search for the rotation pivot */
  protected static int findRotation(int[] nums) {
    return findRotation(nums, 0, nums.length - 1);
  }

  /** Binary searches with left and right limits */
  private static int binarySearch(int target, List<Integer> items, int left, int right) {
    if (right < left) {
      // exhausted: search space: target is not found.
      return -1;
    }

    // check for match on middle element
    int middle = (right - left) / 2 + left;
    int midValue = items.get(middle);
    if (target == midValue) {
      return middle;
    }

    // recusively search for target in left or right subarrays
    if (target < midValue) {
      return binarySearch(target, items, 0, middle - 1);
    }
    return binarySearch(target, items, middle + 1, right);
  }

  /** Binary searches for the target value in the items &amp; returns its index if found. */
  protected static int binarySearch(int target, List<Integer> items) {
    return binarySearch(target, items, 0, items.size() - 1);
  }

  /** Defines a list backed by a rotated array with the given offset */
  protected static final class RotatedArrayList<T> extends ArrayList<T> {
    private static final long serialVersionUID = 42L; // set arbitrarily to 42.
    private final int rotationOffset;

    RotatedArrayList(int initialCapacity, int rotationOffset) {
      super(initialCapacity);
      this.rotationOffset = rotationOffset;
    }

    RotatedArrayList(Collection<T> collection, int rotationOffset) {
      super(collection);
      this.rotationOffset = rotationOffset;
    }

    @Override
    public T get(int index) {
      if (index < 0 || index >= size()) {
        throw new IndexOutOfBoundsException(
            String.format("Given index %d is out of bounds (%d, %d)", index, 0, size() - 1));
      }
      return super.get((index + rotationOffset) % size());
    }

    /** reverse the corrected index to give the index in the original rotated collection */
    protected int reverse(int index) {
      if (index < 0 || index >= size()) {
        throw new IndexOutOfBoundsException(
            String.format("Given index %d is out of bounds (%d, %d)", index, 0, size() - 1));
      }

      return (index + rotationOffset) % size();
    }
  }
  /**
   * Searches for the given target value in given sorted rotated nums.
   *
   * <p>Searches for the target value in the given nums array in sorted order, but may be rotated
   * around a pivot. The integers in the given nums must be unique.
   *
   * @param nums the array of sorted rotated nums to search for target value.
   * @param target value to search for in the given nums array.
   * @return the index of the given if query was found, -1 otherwise.
   */
  public int search(int[] nums, int target) {
    // find rotation offset
    int rotationOffset = findRotation(nums);

    // add nums a rotated nums list
    RotatedArrayList<Integer> rotatedNums = new RotatedArrayList<>(nums.length, rotationOffset);
    for (int num : nums) {
      rotatedNums.add(num);
    }

    // find target
    int rotatedIndex = binarySearch(target, rotatedNums);
    return (rotatedIndex == -1) ? -1 : rotatedNums.reverse(rotatedIndex);
  }
}
