/*
 * Cracking the Coding Interview
 * Chapter 1
 * 8. Zero Matrix
 * Solution tests
 */

package main_test

import (
	"fmt"
	"reflect"
	"strings"
	"testing"

	"github.com/mrzzy/ctci/chapter_1/zero_matrix"
)

// renders the given matrix as a string
func toString(matrix main.Matrix2D) string {
	height, width := len(matrix), len(matrix[0])
	rowStrs := make([]string, height)
	for r, row := range matrix {
		// compile strings for each element of row
		elementStrs := make([]string, width)
		for i, value := range row {
			elementStrs[i] = fmt.Sprintf("%d", value)
		}

		rowStrs[r] = "|" + strings.Join(elementStrs, ", ") + "|"
	}
	return strings.Join(rowStrs, "\n")
}

func TestZeroMatrix(t *testing.T) {
	tests := []struct {
		name     string
		matrix   main.Matrix2D
		expected main.Matrix2D
	}{
		{
			name:     "special case: no elements",
			matrix:   main.Matrix2D{[]int{}},
			expected: main.Matrix2D{[]int{}},
		},
		{
			name:     "special case: one element",
			matrix:   main.Matrix2D{[]int{1}},
			expected: main.Matrix2D{[]int{1}},
		},
		{
			name: "2 by 2 matrix",
			matrix: main.Matrix2D{
				[]int{1, 2},
				[]int{0, 4},
			},
			expected: main.Matrix2D{
				[]int{0, 2},
				[]int{0, 0},
			},
		},
		{
			name: "2 by 4 matrix",
			matrix: main.Matrix2D{
				[]int{1, 2, 3, 4},
				[]int{0, 6, 7, 8},
			},
			expected: main.Matrix2D{
				[]int{0, 2, 3, 4},
				[]int{0, 0, 0, 0},
			},
		},
		{

			name: "4 by 4 matrix with two zeros",
			matrix: main.Matrix2D{
				[]int{1, 2, 3, 4},
				[]int{0, 6, 7, 8},
				[]int{9, 10, 0, 12},
				[]int{12, 14, 15, 16},
			},
			expected: main.Matrix2D{
				[]int{0, 2, 0, 4},
				[]int{0, 0, 0, 0},
				[]int{0, 0, 0, 0},
				[]int{0, 14, 0, 16},
			},
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			actual := main.ZeroMatrix(test.matrix)
			if !reflect.DeepEqual(actual, test.expected) {
				t.Errorf("got: %s\n expected: %s", toString(actual), toString(test.expected))
			}
		})
	}
}
