/*
 * Cracking the Coding Interview
 * Chapter 2
 * 2.2 Return Kth to Last
 */

package kth_last_element_test

import (
	"container/list"
	kth "kth_last_element"
	"testing"
)

func toLinkedList(slice []interface{}) *list.List {
	l := list.New()
	for i := range slice {
		l.PushBack(slice[i])
	}

	return l
}

func TestKLastElement(t *testing.T) {
	linkedList := toLinkedList([]interface{}{3, 7, 5, 2, 8, 4})

	tests := []struct {
		name     string
		query    kth.LastElementQuery
		expected interface{}
	}{
		{
			name: "Get 2nd last element from linked list",
			query: kth.LastElementQuery{
				LinkedList: linkedList.Front(),
				Offset:     1,
			},
			expected: 8,
		},
		{
			name: "Get last element from linked list",
			query: kth.LastElementQuery{
				LinkedList: linkedList.Front(),
				Offset:     0,
			},
			expected: 4,
		},
		{
			name: "Get 5th element from linked list",
			query: kth.LastElementQuery{
				LinkedList: linkedList.Front(),
				Offset:     5,
			},
			expected: 3,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			element, _, err := kth.KLastElement(test.query)
			if err != nil {
				t.Errorf("Unexpected error: %v", err)
			}
			if value := element.(int); value != test.expected {
				t.Errorf("Got value = %d, expected value = %d", value, test.expected)
			}
		})
	}
}
