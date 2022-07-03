/*
 * Cracking the Coding Interview
 * Chapter 2
 * 2.2 Return Kth to Last
 */

package kth_last_element

import (
	"container/list"
	"fmt"
)

type LastElementQuery struct {
	LinkedList *list.Element
	Offset     uint
	length     uint
}

// Get & return the kth last element from the given linked list.
// The element retrieved is specified as an offset from the last element of the list.
// Although the golang stdlib linked list implementation is doublely linked, this
// solution assumes that the given list is singlely linked as specifyed in the question.
// returns the kth last element or the relative offset to the last element.
func KLastElement(query LastElementQuery) (interface{}, uint, error) {
	// base case no more elements: found length of linked list
	if query.LinkedList == nil {
		// check if linked list has enough elements to support offset
		if query.length < query.Offset {
			return nil, 0, fmt.Errorf(
				"Query offset %d is out of bounds"+
					"for the given linked list of length %d", query.Offset, query.length)
		}
		return nil, query.Offset, nil
	}

	// attempt to find the kth last element in the list recursively
	element, offset, err := KLastElement(LastElementQuery{
		LinkedList: query.LinkedList.Next(),
		Offset:     query.Offset,
		length:     query.length + 1,
	})
	if err != nil {
		return nil, 0, err
	}
	// check if recursive call has already found the element, if so return found element
	if element != nil {
		return element, 0, nil
	}
	// check if we have found the element, if so return it
	if offset == 0 {
		return query.LinkedList.Value, 0, nil
	}

	// element not yet found, decrement the traversed offset
	return nil, offset - 1, nil
}
