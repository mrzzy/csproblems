/*
 * Leetcode
 * XXX. PROBLEM
 * Solution tests
 *
 */

package solution

import "testing"

func TestSolution(t *testing.T) {
	tests := []struct {
		name         string
		num          uint32
		expectedBits int
	}{
		{
			name:         "special case: no bits set",
			num:          0b00000000000000000000000000000000,
			expectedBits: 0,
		},
		{
			name:         "special case: 1 bit set start",
			num:          0b10000000000000000000000000000000,
			expectedBits: 1,
		},
		{
			name:         "special case: 1 bit set end",
			num:          0b00000000000000000000000000000001,
			expectedBits: 1,
		},
		{
			name:         "5 bits set",
			num:          0b10000010000101000000000000100000,
			expectedBits: 5,
		},
		{
			name:         "8 bits set",
			num:          0b10100010000101100100000000100000,
			expectedBits: 8,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			if actualBits := hammingWeight(test.num); actualBits != test.expectedBits {
				t.Errorf("Expected nBits: %d Got nBits: %d", test.expectedBits, actualBits)
			}
		})
	}
}
