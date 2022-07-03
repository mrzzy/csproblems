/*
 * Leetcode
 * 152. Maximum Product Subarray
 * Solution
 *
 */

package solution

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

// Find & return the maximum product of any subarray of the given nums.
// nums - array of integers, -10 <= i <= 10 that must contain at least one element.
// Subarray considered must be contiguous.
func maxProduct(nums []int) int {
	if len(nums) <= 1 {
		return nums[0]
	}

	// current minimum product
	currentMin := nums[0]
	// current maximum product
	currentMax := nums[0]
	// overall minimum product
	overallMax := nums[0]

	for _, n := range nums[1:] {
		// maximum product is the max of:
		// * extending the current subarray to the the current elemnmt
		// * starting a new subarray with the current element
		if n >= 0 {
			currentMin = min(currentMin*n, n)
			currentMax = max(currentMax*n, n)
		} else {
			// negative nums invert the computed product, so we use the inverse
			// max instead (ie to compute min we use the current max)
			newMax := max(currentMin*n, n)
			newMin := min(currentMax*n, n)
			currentMax, currentMin = newMax, newMin
		}

		overallMax = max(currentMax, overallMax)
	}

	return overallMax
}
