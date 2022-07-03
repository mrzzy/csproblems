/*
Leetcode
191. Number of 1 Bits
Solution
*/

package solution

// Calculate & return the hamming weight of the given num interpreted as binary string.
// The hamming weight of a binary string is defined as the no. of 1 bits in the string.
func hammingWeight(num uint32) int {
	nBits := 0
	for i := 0; i < 32; i++ {
		// check bit at position i is set by performing a bitwise AND
		// revert the bitwise left shift to get a value between 0 or 1 depend if the bit is set
		// cast required to ensure that we do not bitwise and signed & unsigned ints together
		nBits += int(((uint32(1) << i) & num) >> i)
	}
	return nBits
}
