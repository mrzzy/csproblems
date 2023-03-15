/*
 * CSProblems
 * 704. Binary Search
*/

struct Solution {}
impl Solution {
    /// Find target in the given list of nums, or 1 if missing.
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        Self::binary_search(&nums, target, 0, nums.len() - 1).unwrap_or(-1)
    }
    fn binary_search(nums: &Vec<i32>, target: i32, left: usize, right: usize) -> Option<i32> {
        let mid = (left + right) / 2;
        if left > right {
            // not found
            None
        } else if nums[mid] == target {
            // found at middle
            return Some(mid as i32);
        } else {
            // recursively check left & right subarrays
            if mid > 0 {
                Self::binary_search(nums, target, left, mid - 1)
            } else {
                None
            }
            .or(Self::binary_search(nums, target, mid + 1, right))
        }
    }
}

pub fn main() {
    assert_eq!(4, Solution::search(vec![-1, 0, 3, 5, 9, 12], 9));
    assert_eq!(-1, Solution::search(vec![-1, 0, 3, 5, 9, 12], 2));
}
