/*
 * Cracking the Coding Interview
 * Chapter 1
 * 3. Urlify
 */

package urlify

// Converts the spaces in the given byte array to url form: '%20' in place.
// takes in a byte array repersenting a string to converted padded with space required
func Urlify(chars *[]byte) {
	// copy given characters out of chars so that we can continue to reference
	// input characters while we perform in place updates on chars
	inputChars := make([]byte, len(*chars))
	copy(inputChars, *chars)

	// search for the start of padding spaces at the end of input string
	padBegin := 0
	for i := len(inputChars) - 1; i >= 0 && inputChars[i] == ' '; i-- {
		padBegin = i
	}

	if padBegin == 0 {
		// everything in the input string is padding spaces, nothing to do
		return
	}

	// translate input str into url form
	writeIdx := 0
	for _, c := range inputChars[:padBegin] {
		switch c {
		case ' ':
			// translate ' ' to url form '%20'
			(*chars)[writeIdx] = '%'
			(*chars)[writeIdx+1] = '2'
			(*chars)[writeIdx+2] = '0'

			writeIdx += 3
		default:
			(*chars)[writeIdx] = c
			writeIdx++
		}
	}
}
