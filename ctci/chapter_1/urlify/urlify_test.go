/*
 * Cracking the Coding Interview
 * Chapter 1
 * 3. Urlify tests
 */

package urlify_test

import (
	"bytes"
	"testing"
	"urlify"
)

func TestUrlify(t *testing.T) {
	tests := []struct {
		name     string
		chars    []byte
		expected []byte
	}{
		{
			name:     "should convert to url form: 'hello world'",
			chars:    []byte("hello world  "),
			expected: []byte("hello%20world"),
		},
		{
			name:     "should convert multiple spaces to url form 'there are multiple spaces'",
			chars:    []byte("there are multiple spaces      "),
			expected: []byte("there%20are%20multiple%20spaces"),
		},
		{
			name:     "should do nothing on empty input: ''",
			chars:    []byte(""),
			expected: []byte(""),
		},
		{
			name:     "should do nothing given all spaces: '     '",
			chars:    []byte("     "),
			expected: []byte("     "),
		},
		{
			name:     "should do nothing when no spaces in input: 'a-string'",
			chars:    []byte("a-string"),
			expected: []byte("a-string"),
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			urlify.Urlify(&test.chars)

			if bytes.Compare(test.chars, test.expected) != 0 {
				t.Errorf("%s is not equal to %s", test.chars, test.expected)
			}
		})
	}
}
