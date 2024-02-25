/*
 * CS Problems
 * Leetcode
 * 200. Number of Islands
*/
object Solution {
  type Grid = Array[Array[Char]]
  type IslandMap = Map[(Int, Int), Int]

  def floodFill(
      grid: Grid,
      islandMap: IslandMap,
      position: (Int, Int),
      islandId: Int
  ): (IslandMap, Boolean) = {
    val (r, c) = position

    // check if position is valid for flood filling
    if (
      r < 0 ||
      r > grid.length - 1 ||
      c < 0 ||
      c > grid(0).length - 1 ||
      grid(r)(c) == '0' ||
      islandMap.contains((r, c))
    ) {
      (islandMap, false)
    } else {
      // fill current position
      var filledMap = islandMap + (position -> islandId)
      // recursively fill adjacent positions
      // top
      filledMap = floodFill(grid, filledMap, (r - 1, c), islandId)._1
      // bottom
      filledMap = floodFill(grid, filledMap, (r + 1, c), islandId)._1
      // left
      filledMap = floodFill(grid, filledMap, (r, c - 1), islandId)._1
      // right
      filledMap = floodFill(grid, filledMap, (r, c + 1), islandId)._1
      (filledMap, true)
    }
  }

  def numIslands(grid: Grid): Int = {
    case class State(
        islandId: Int = 0,
        islandMap: IslandMap = Map()
    )
    val State(islandId, _) = grid.zipWithIndex.foldLeft(State()) {
      case (state, (row, r)) => {
        row.zipWithIndex.foldLeft(state) {
          case (State(islandId, islandMap), (land, c)) => {
            // mark all surrounding positions as belong to this island
            val (nextMap, isFilled) =
              floodFill(grid, islandMap, (r, c), islandId)
            State(islandId + (if (isFilled) 1 else 0), nextMap)
          }
        }
      }
    }
    // no. of islands correspond to island id
    islandId
  }
}
object Solution {
  type Grid = Array[Array[Char]]
  type IslandMap = Map[(Int, Int), Int]

  def floodFill(
      grid: Grid,
      islandMap: IslandMap,
      position: (Int, Int),
      islandId: Int
  ): (IslandMap, Boolean) = {
    val (r, c) = position

    // check if position is valid for flood filling
    if (
      r < 0 ||
      r > grid.length - 1 ||
      c < 0 ||
      c > grid(0).length - 1 ||
      grid(r)(c) == '0' ||
      islandMap.contains((r, c))
    ) {
      (islandMap, false)
    } else {
      // fill current position
      var filledMap = islandMap + (position -> islandId)
      // recursively fill adjacent positions
      // top
      filledMap = floodFill(grid, filledMap, (r - 1, c), islandId)._1
      // bottom
      filledMap = floodFill(grid, filledMap, (r + 1, c), islandId)._1
      // left
      filledMap = floodFill(grid, filledMap, (r, c - 1), islandId)._1
      // right
      filledMap = floodFill(grid, filledMap, (r, c + 1), islandId)._1
      (filledMap, true)
    }
  }

  def numIslands(grid: Grid): Int = {
    case class State(
        islandId: Int = 0,
        islandMap: IslandMap = Map()
    )
    val State(islandId, _) = grid.zipWithIndex.foldLeft(State()) {
      case (state, (row, r)) => {
        row.zipWithIndex.foldLeft(state) {
          case (State(islandId, islandMap), (land, c)) => {
            // mark all surrounding positions as belong to this island
            val (nextMap, isFilled) =
              floodFill(grid, islandMap, (r, c), islandId)
            State(islandId + (if (isFilled) 1 else 0), nextMap)
          }
        }
      }
    }
    // no. of islands correspond to island id
    islandId
  }
}
