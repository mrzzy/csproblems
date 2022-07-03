/*
 * Cracking the Coding Interview
 * Linked Lists
 * 3.1 Remove Dups
 */

#include <cassert>
#include <iostream>
#include <list>
#include <memory>
#include <unordered_set>

using namespace std;

/** @brief remove duplicates in the given list of integers with O(1) space.
 *
 * @param linked list of integers to remove duplicates from.
 * @return given linked list with duplicates removed.
 */
unique_ptr<list<int>> removeDups(unique_ptr<list<int>> items) {
  // duplicates are not possible with less than 2 elements
  if (items->size() < 2) {
    return items;
  }

  for (auto i = items->begin(); i != items->end(); i++) {
    // look for duplicates to item i
    auto j = i;
    j++;
    while (j != items->end()) {
      if (*i == *j) {
        // found duplicate: mark for removal with INT32_MIN
        *j = INT32_MIN;
      }
      j++;
    }
  }

  // remove marked duplicates with INT32_MIN
  for (auto i = items->begin(); i != items->end();) {
    if (*i == INT32_MIN) {
      i = items->erase(i);
      continue;
    }
    i++;
  }

  return items;
}

// verifies that removeDups() given the inputs returns expected out
void testRemoveDups(const initializer_list<int> &inputs,
                    const initializer_list<int> &expected) {
  auto actual = removeDups(make_unique<list<int>>(inputs));
  auto expectedSet = unordered_set<int>(expected);

  for (int i : *actual) {
    expectedSet.erase(i);
  }
  assert(expectedSet.size() == 0);
}

int main() {
  testRemoveDups({}, {});
  testRemoveDups({1}, {1});
  testRemoveDups({1, 1}, {1});
  testRemoveDups({3, 7, 3, 8, 2, 1, 8, 1}, {1, 2, 3, 7, 8});
  testRemoveDups({6, 2, 8, 4, 2, 2, 6, 7, 1}, {6, 2, 8, 4, 7, 1});
}
