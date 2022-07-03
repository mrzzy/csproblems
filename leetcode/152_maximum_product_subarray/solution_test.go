/*
 * Leetcode
 * 152. Maximum Product Subarray
 * Solution tests
 *
 */

package solution

import "testing"

func TestMaxProduct(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "special case: 1 element",
			nums:     []int{1},
			expected: 1,
		},
		{
			name:     "special case: zeros",
			nums:     []int{0, 0, 0, 0},
			expected: 0,
		},
		{
			name:     "nums with no negatives",
			nums:     []int{5, 2, 7, 3, 1},
			expected: 210,
		},
		{
			name:     "nums with all negative",
			nums:     []int{-6, -2, -4, -7, -1},
			expected: 336,
		},
		{
			name:     "nums with even no.of negatives",
			nums:     []int{5, -9, 3, -6, 1},
			expected: 810,
		},
		{
			name:     "nums with odd num of negatives",
			nums:     []int{2, 3, -2, 4},
			expected: 6,
		},
		{
			name:     "nums with zeros",
			nums:     []int{2, 3, 0, 4, 2},
			expected: 8,
		},
		{
			name:     "",
			nums:     []int{2, -1, 1, 1},
			expected: 2,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			if actual := maxProduct(test.nums); actual != test.expected {
				t.Errorf("got = %d, expected = %d", actual, test.expected)
			}
		})
	}

}
