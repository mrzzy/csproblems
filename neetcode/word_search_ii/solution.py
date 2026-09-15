#
# Neetcode
# 77. Word Search II
# Python Solution
#


from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False

    def insert(self, word: str):
        if len(word) <= 0:
            # mark word ending
            self.is_word = True
            return

        # recursively insert word into trie
        letter = word[0]
        self.children[letter].insert(word[1:])


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        matches = []
        for i in range(len(board)):
            for j in range(len(board[0])):

                # match words starting at (i, j), assuming letters already checked
                def match_words(
                    i: int, j: int, trie: Trie, letters: list[str], seen: set
                ):
                    position = (i, j)
                    if position in seen:
                        # position already checked
                        return

                    letters.append(board[i][j])
                    seen.add(position)

                    # record word match if any
                    if trie.is_word == True:
                        matches.append("".join(letters))
                        # clear word match
                        trie.is_word = False
                    # recursively check positions for matches
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + x, j + y
                        # check bounds
                        if not (0 <= ni < len(board) and 0 <= nj < len(board[0])):
                            continue
                        next_letter = board[ni][nj]
                        if next_letter in trie.children:
                            match_words(
                                ni, nj, trie.children[next_letter], letters, seen
                            )

                    letters.pop()
                    seen.remove(position)

                letter = board[i][j]
                if letter in trie.children:
                    match_words(i, j, trie.children[letter], [], set())
        return matches
