class SolutionSpec extends munit.FunSuite {
  test("test case 2") {
    val grid =
      Array(
        Array('1', '1', '0', '0', '0'),
        Array('1', '1', '0', '0', '0'),
        Array('0', '0', '1', '0', '0'),
        Array('0', '0', '0', '1', '1')
      )
    println(f"islands: ${Solution.numIslands(grid)}")
  }
}
