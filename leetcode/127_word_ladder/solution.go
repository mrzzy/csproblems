//
// CS Problems
// Leetcode
// 127. Word Ladder
//

func ladderLength(beginWord string, endWord string, wordList []string) int {
	// convert wordlist into map for O(1) lookup
	type wordSet map[string]bool
	words := wordSet{}
	for _, word := range wordList {
		words[word] = true
	}

	// explore words with BFS to find shortest path
	type explore struct {
		word  string
		depth int
	}
	queue := make([]explore, 0)
	queue = append(queue, explore{beginWord, 1})

	for len(queue) > 0 {
		next := queue[0]
		queue = queue[1:]

		// check if we found start word
		if next.word == endWord {
			return next.depth
		}

		// try replacing characters in words to look for connections within wordlist
		for i := 0; i < len(next.word); i++ {
			for l := uint8('a'); l <= uint8('z'); l++ {
				letter := string(rune(l))
				altered := next.word[:i] + letter + next.word[i+1:]

				if _, ok := words[altered]; ok {
					queue = append(queue, explore{altered, next.depth + 1})
					// since we are doing BFS, this is already the shortest path to
					// the word, so we can remove it from wordset to prevent cycles
					delete(words, altered)
				}
			}
		}

	}

	return 0
}
