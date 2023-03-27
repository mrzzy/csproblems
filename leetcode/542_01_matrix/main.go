//
// CS Problems
// Leetcode
// 542. 01 Matrix
//

package main

import (
	"fmt"
	"math"
)

// Defines an instruction to fill row <r>, column <c> with <value>.
type Fill struct {
	r     int
	c     int
	value int
}

// Queue adjacent matrix cells for updates into the given toFill queue.
func queueAdjacent(r int, c int, value int, minDist [][]int, toFill []Fill) []Fill {
	if r > 0 {
		// top
		toFill = append(toFill, Fill{r: r - 1, c: c, value: value})
	}
	if c < len(minDist[0])-1 {
		// right
		toFill = append(toFill, Fill{r: r, c: c + 1, value: value})
	}
	if r < len(minDist)-1 {
		// bottom
		toFill = append(toFill, Fill{r: r + 1, c: c, value: value})
	}
	if c > 0 {
		// left
		toFill = append(toFill, Fill{r: r, c: c - 1, value: value})
	}

	return toFill
}

func updateMatrix(mat [][]int) [][]int {
	if len(mat) <= 0 {
		// empty matrix: do nothing
		return mat
	}

	height, width := len(mat), len(mat[0])
	// init min distance matrix to track distance to 0
	minDist := make([][]int, height)
	toFill := make([]Fill, 0)
	for r, row := range mat {
		minDist[r] = make([]int, width)
		for c, value := range row {
			minDist[r][c] = math.MaxInt32
			if value == 0 {
				// already on a 0, so distance to 0 is 0
				toFill = append(toFill, Fill{r: r, c: c, value: 0})
			}
		}
	}

	// fill min distances according to fill queue
	for len(toFill) > 0 {
		fill := toFill[0]
		// utilise fill only if it gives us a smaller distance
		if fill.value < minDist[fill.r][fill.c] {
			// queue fills for adjacent cells as it potential to give us a smaller distance
			// via this cell
			minDist[fill.r][fill.c] = fill.value
			toFill = queueAdjacent(fill.r, fill.c, fill.value+1, minDist, toFill)
		}
		toFill = toFill[1:]
	}

	return minDist
}

func main() {
	fmt.Printf("%v\n", updateMatrix([][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}))
	fmt.Printf("%v\n", updateMatrix([][]int{{1, 1, 1}, {0, 1, 0}, {1, 1, 1}}))
}
