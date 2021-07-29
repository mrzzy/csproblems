/*
 * leetcode
 * 11. Container With Most Water
 */

#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class Solution {
 public:
  using index_t = vector<int>::size_type;

  /* Compute the area delimited by leftPillar & rightPillar.
   * Obtains the heights of left & right pillar from the given heights.
   * Returns the computed area.
   */
  int area(const vector<int>& heights, index_t leftPillar,
           index_t rightPillar) {
    return abs(static_cast<int>(leftPillar - rightPillar)) *
           min(heights[leftPillar], heights[rightPillar]);
  }

  /*
   * Compute the maximum area delimited by pillars of the given heights.
   * Takes in a vector height where height[i] determines the height of pillar.
   * Returns the maximum area possible delimited by any two pillars.
   */
  int maxArea(vector<int>& heights) {
    // start with pillars at the each end: heuristic that pillars with
    // biggest distance from each other would give the max area.
    index_t i = 0;
    index_t j = heights.size() - 1;

    int maxAreaSoFar = 0;
    while(i != j) {
      // update max area so far
      maxAreaSoFar = max(area(heights, i, j), maxAreaSoFar);

      // now we have to scarifice 1 unit of distance between pillars
      // by selecting a new pillar i or j.
      // since area is bounded by min(heights[i], heights[j]), it makes 
      // we should only move:
      // * i if heights[i] < heights[j] as moving j will not improve area as its bounded by min(...)
      // * j if heights[j] < heights[i] as moving i will not improve area as its bounded by min(...)
      // * i if heights[i] == heights[j] to break tie as i or j would be equally likely to improve area
      if(heights[i] < heights[j]) {
        i += 1;
      } else if(heights[i] > heights[j]) {
        j -= 1;
      } else {
        i += 1;
      }
    }
    
    return maxAreaSoFar;
  }
};


int main() {
  Solution solution;
  // test area function
  assert(solution.area(vector<int>{0, 0}, 0, 1) == 0);
  assert(solution.area(vector<int>{0, 1}, 0, 1) == 0);
  assert(solution.area(vector<int>{1, 0}, 0, 1) == 0);
  assert(solution.area(vector<int>{2, 2}, 0, 1) == 2);
  assert(solution.area(vector<int>{1, 7, 8, 9, 2}, 1, 3) == 14);

  // test solution
  vector<int> v1{2, 2};
  assert(solution.maxArea(v1) == 2);

  vector<int> v2{1, 7, 8, 9, 2};
  assert(solution.maxArea(v2) == 14);

  vector<int> v3{5, 1, 4, 2, 4};
  assert(solution.maxArea(v3) == 16);

  vector<int> v4{1, 4, 10, 6, 4};
  assert(solution.maxArea(v4) == 12);

  ifstream v5File("tests/test_v5.txt");
  vector<int> v5;
  for(string intStr; getline(v5File, intStr, ',');) {
    v5.push_back(stoi(intStr));
  }
  assert(solution.maxArea(v5) == 402471897);
  cout << "PASS" << endl;
}
