#
# Neetcode
# 78. Word Ladder
# Python Solution
#

from collections import deque


def edit(w1: str, w2: str):
    """Compute edit distance between w1 and w2"""
    if len(w1) != len(w2):
        raise ValueError("Words must be same length")

    n_edits = 0
    for i in range(len(w1)):
        n_edits += w1[i] != w2[i]

    return n_edits


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # build adjacent list of word edit distances
        wordList.append(beginWord)
        begin_i = len(wordList) - 1

        n_words = len(wordList)
        n_edits = [[0 for _ in range(n_words)] for _ in range(n_words)]

        for i, w1 in enumerate(wordList):
            for j, w2 in enumerate(wordList):
                n_edits[i][j] = edit(w1, w2)

        # bfs to find shortest path to end word
        frontier = deque([(begin_i, 0)])
        seen = set()
        while len(frontier) > 0:
            i, i_edits = frontier.popleft()
            if wordList[i] == endWord:
                # length of transformation sequence: n_edits + 1
                return i_edits + 1

            # mark word at i as seen
            seen.add(i)

            # iterate word's neighbours
            for j, n_edit in enumerate(n_edits[i]):
                # skip if not accessible due to edit distance or already seen
                if n_edit > 1 or j in seen:
                    continue

                frontier.append((j, i_edits + 1))

        # not found
        return 0
