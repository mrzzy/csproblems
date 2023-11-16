//
// CS Problems
// Leetcode
// 208. Implement Trie (Prefix Tree)
//
package main

type Trie struct {
	// whether a word stored in this trie end here
	isEnd bool
	// reference to next nodes of the trie
	// 26: 26 possible english characters
	next [26]*Trie
}

func Constructor() Trie {
	return Trie{
		isEnd: false,
	}
}

func (this *Trie) Insert(word string) {
	node, remainderIdx := this.walk(word)
	// insert nodes for characters of the word
	if remainderIdx != -1 {
		for i := remainderIdx; i < len(word); i++ {
			next := &Trie{
				isEnd: false,
			}
			node.next[word[i]-'a'] = next
			node = next
		}
	}

	/// mark last node as the end
	node.isEnd = true
}

func (this *Trie) Search(word string) bool {
	node, remainderIdx := this.walk(word)
	return node.isEnd && remainderIdx == -1
}

func (this *Trie) StartsWith(prefix string) bool {
	node, remainderIdx := this.walk(prefix)
	return node != nil && remainderIdx == -1
}

// Walk the Trie guided by 'prefix'
// Returns the last node that matches prefix and the index to the remaining prefix that does not match.
func (this *Trie) walk(prefix string) (*Trie, int) {
	current := this
	for i, c := range prefix {
		// advance node based on next character of the prefix
		next := current.next[c-'a']
		if next == nil {
			// mismatch in prefix: no match found
			return current, i
		}
		current = next
	}
	// matched prefix: return matched node
	return current, -1
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
