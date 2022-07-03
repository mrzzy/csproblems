/*
 * Cracking the Coding Interview
 * Chapter 1
 * 8. Zero Matrix
 * Solution
 */

package main

import "fmt"

// represents a 2 dimensional matrix row-major
type Matrix2D = [][]int

// initializes a new matrix 2d
func NewMatrix2D(height int, width int) (Matrix2D, error) {
	if height < 0 || width < 0 {
		return nil, fmt.Errorf("Cannot create matrix with negative dimensions")
	}

	matrix := make(Matrix2D, height)
	for i := range matrix {
		matrix[i] = make([]int, width)
	}
	return matrix, nil
}

// zeros the entire rows & columns where 0 exists in the given len
func ZeroMatrix(matrix Matrix2D) Matrix2D {
	// empty or 1 element matrix: do nothing
	if len(matrix) == 0 || len(matrix) == 1 && len(matrix) == 1 {
		return matrix
	}

	// tabulate the rows and column to be zeroed
	zeroRows, zeroCols := map[int]bool{}, map[int]bool{}
	for row := range matrix {
		for col, value := range matrix[row] {
			if value == 0 {
				// mark row and column with zero for zeroing
				zeroRows[row], zeroCols[col] = true, true
			}
		}
	}

	// render zeroed matrix
	height, width := len(matrix), len(matrix[0])
	zeroedMatrix, _ := NewMatrix2D(height, width)

	for row := 0; row < height; row++ {
		// skip zeroed rows
		if ok, _ := zeroRows[row]; ok {
			continue
		}
		for col := 0; col < width; col++ {
			// skip zeroed columns
			if ok, _ := zeroCols[col]; ok {
				continue
			}

			// copy non zeroed value from original matrix
			zeroedMatrix[row][col] = matrix[row][col]
		}
	}

	return zeroedMatrix
}
