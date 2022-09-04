#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

/** 2D square array representing a board of black (1) or white (0) squares */
using Board = vector<vector<int>>;

class Solution {
  using size_t = vector<int>::size_type;

public:
  /**
   * Compute the no. of swaps needed to convert the given board into a
   * chessboard.
   *
   * @param A square board of length 2-30 with 0 or 1 elements used to to
   * represent black (1) or white (0) squares respectively.
   * @returns The no. of moves needed to solve, or -1 if the board is
   * unsolvable.
   */
  int movesToChessboard(Board &board) {
    if (!isSolvable(board)) {
      return -1;
    }
    int minMovesRows = min(movesAlternatingRows(board, 0), movesAlternatingRows(board, 1));
    int minMovesCols = min(movesAlternatingCols(board, 0), movesAlternatingCols(board, 1));

    return minMovesRows + minMovesCols;
  }

  // Compute the min  no. of swaps needed to form alternating rows, assuming
  // the color of the top left square.  If unsolvable, returns int max.
  int movesAlternatingRows(const Board &board, int topLeft) {
    // identify columns out of place
    int nMisplacedRows = 0;
    for (int r = 0; r < static_cast<int>(board.size()); r++) {
      if(board[r][0] != (r + topLeft) % 2) {
        nMisplacedRows ++;
      }
    }
    // check for solvablity with swaps
    if(nMisplacedRows % 2 != 0) {
      return numeric_limits<int>::max();
    }
    // one swap resolves two misplaces
    return nMisplacedRows / 2;
  }

  // Compute the min  no. of swaps needed to form alternating columns, assuming
  // the color of the top left square.  If unsolvable, returns int max.
  int movesAlternatingCols(const Board &board, int topLeft) {
    // identify columns out of place
    int nMisplacedCols = 0;
    for (int c = 0; c < static_cast<int>(board.size()); c++) {
      if(board[0][c] != (c + topLeft) % 2) {
        nMisplacedCols ++;
      }
    }
    // check for solvablity with swaps
    if(nMisplacedCols % 2 != 0) {
      return numeric_limits<int>::max();
    }
    // one swap resolves two misplaces
    return nMisplacedCols / 2;
  }

  // Check if the chessboard is solvable based on the observation that valid
  // chessboards have 2 patterns of rows / columns distributed relatively equally.
  bool isSolvable(const Board &board) const {
    // check dimensions of board is above 2 & square
    if(board.size() < 2 || board.size() != board[0].size()) {
      return false;
    }

    // check board only contains 1 / 0
    for(auto row: board) {
      for(auto square: row) {
        if (square != 0 && square != 1) {
          return false;
        }
      }
    }

    // calculate how many times each row column pattern occurs
    auto joinPattern = [](string &pattern,  int square) {
            return move(pattern) + to_string(square);
          };
    unordered_map<string, uint32_t> rowPatterns;
    for (uint32_t r = 0; r < board.size(); r++) {
      string pattern = accumulate(board[r].begin(), board[r].end(), string{}, joinPattern);
      rowPatterns[pattern] ++;
    }
    unordered_map<string, uint32_t> colPatterns;
    for (uint32_t c = 0; c < board.size(); c++) {
      vector<int> column;
      for (uint32_t r = 0; r < board.size(); r++) {
        column.push_back(board[r][c]);
      }

      string pattern = accumulate(column.begin(), column.end(), string{}, joinPattern);
      colPatterns[pattern] ++;
    }

    // valid chesssboards have 2 distinct patterns per axis
    if(rowPatterns.size() != 2 || colPatterns.size() != 2) {
      return false;
    }

    // check the 2 patterns are inversions of each other
    auto unpack = [](const unordered_map<string, uint32_t> &patterns) {
      auto iter = patterns.begin();
      auto firstPattern = iter->first;
      auto nFirstPattern = iter->second;
      iter = next(iter);
      auto secondPattern = iter->first;

      return tuple<string, uint32_t, string>{firstPattern, nFirstPattern, secondPattern};
    };

    auto [firstRowPattern, nFirstRowPattern, secondRowPattern] = unpack(rowPatterns);
    if(!isInversion(firstRowPattern, secondRowPattern)) {
      return false;
    }
    auto [firstColPattern, nFirstColPattern, secondColPattern] = unpack(colPatterns);
    if(!isInversion(firstColPattern, secondColPattern)) {
      return false;
    }

    uint32_t half = board.size() / 2;
    if(board.size() % 2 == 0) {
      // even board size: check for half no. of patterns.
      // since there are only 2 patterns for each axis, we only need to check the first one.
      return nFirstRowPattern == half && nFirstColPattern == half;
    }
    // odd board size: check for around half no. of patterns
    return (
      (nFirstRowPattern == half || nFirstRowPattern == half + 1) &&
      (nFirstColPattern == half || nFirstColPattern == half + 1)
    );
  }

  // check whether the two given '0' & '1' patterns are inversions of each other
  bool isInversion(const string &first, const string &second) const {
    if(first.size() != second.size()) {
      return false;
    }
    for (uint32_t i = 0; i < first.size(); i++) {
      if(first[i] == '0' && second[i] != '1') {
        return false;
      }
      if(first[i] == '1' && second[i] != '0') {
        return false;
      }
    }

    return true;
  }
};

void testIsSolvable(const Solution &s) {
  assert(!s.isSolvable(Board{
    vector<int>{0, 0, 0},
    vector<int>{0, 0, 1},
    vector<int>{0, 0, 0},
  }));
  assert(!s.isSolvable(Board{
    vector<int>{1, 1},
    vector<int>{0, 0}
  }));
  assert(s.isSolvable(Board{
    vector<int>{1, 0},
    vector<int>{0, 1}
  }));
  assert(!s.isSolvable(Board{
    vector<int>{2, 0}, 
    vector<int>{0, 2}
  }));
  assert(!s.isSolvable(Board{
    vector<int>{1, 0, 1},
    vector<int>{0, 1, 1},
    vector<int>{1, 0, 1},
  }));
  // [[1,1,1,0],[1,1,1,0],[0,0,0,1],[0,0,0,1]]
  assert(!s.isSolvable(Board{
    vector<int>{1, 1, 1, 0},
    vector<int>{1, 1, 1, 0},
    vector<int>{0, 0, 0, 1},
    vector<int>{0, 0, 0, 1},
  }));
}

void testMovesToChessboard(Solution &s) {
  auto b = Board{vector<int>{1, 0}, vector<int>{0, 1}};
  assert(s.movesToChessboard(b) == 0);

  b = Board{vector<int>{0, 1}, vector<int>{1, 0}};
  assert(s.movesToChessboard(b) == 0);

  b = Board{
    vector<int>{1, 0, 1},
    vector<int>{0, 1, 0},
    vector<int>{1, 0, 1},
  };
  assert(s.movesToChessboard(b) == 0);

  b = Board{
    vector<int>{1, 0, 1},
      vector<int>{1, 0, 1},
      vector<int>{0, 1, 0},
  };
  assert(s.movesToChessboard(b) == 1);

  b = Board{
      vector<int>{1, 1, 0, 1, 0, 0},
      vector<int>{0, 0, 1, 0, 1, 1},
      vector<int>{1, 1, 0, 1, 0, 0},
      vector<int>{0, 0, 1, 0, 1, 1},
      vector<int>{1, 1, 0, 1, 0, 0},
      vector<int>{0, 0, 1, 0, 1, 1},
  };
  assert(s.movesToChessboard(b) == 1);

  b = Board{
      vector<int>{0, 1, 0, 1, 1, 0, 0},
      vector<int>{1, 0, 1, 0, 0, 1, 1},
      vector<int>{0, 1, 0, 1, 1, 0, 0},
      vector<int>{0, 1, 0, 1, 1, 0, 0},
      vector<int>{1, 0, 1, 0, 0, 1, 1},
      vector<int>{0, 1, 0, 1, 1, 0, 0},
      vector<int>{1, 0, 1, 0, 0, 1, 1},
  };
  assert(s.movesToChessboard(b) == 3);
}

int main() {
  Solution s;
  testIsSolvable(s);
  testMovesToChessboard(s);
}
