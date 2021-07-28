/*
 * Leetcode
 * 295. Find Median from Data Stream
*/

#include <cmath>
#include <vector>
#include <sstream>
#include <numeric>
#include <iostream>
#include <stdexcept>
#include <algorithm>

using namespace std;
/** @brief Pushes the given value into the heap-ordered vector */
void pushHeap(vector<int>& heapVec, int value)
{
    heapVec.push_back(value);
    push_heap(heapVec.begin(), heapVec.end());
}

/** @brief Pops & returns  the value from the given heap-ordered vector */
int popHeap(vector<int>& heapVec)
{
    pop_heap(heapVec.begin(), heapVec.end());
    int value = heapVec.back();
    heapVec.pop_back();

    return value;
}

/** @brief Finds the median of a stream of numbers added with addNum() */
class MedianFinder
{
public:
    /** @brief Max heap of the lower half the added numbers */
    vector<int> lowerHalfMaxHeap;

    /** @brief Min heap of the upper half the added numbers.
     *
     * Implemented as max heap of negative numbers to simulate a min heap.
    */
    vector<int> upperHalfMinHeap;

    /**
     * @brief Adds the given integer into this MedianFinder.
     * Adds the given integer into the MedianFinder. The median of the added
     * integers can then be retrieved with findMedian().
     *
     * @param num The integer to add to this MedianFinder.
    */
    void addNum(int num)
    {
        if(size() <= 0)
        {
            // no elements in heaps yet: just add num to lower half heap
            lowerHalfMaxHeap.push_back(num);
        }
        // use max int of lowerHalfMaxHeap as pivot partitioning between
        // lower & upper half heaps
        else if(num <= lowerHalfMaxHeap.front())
        {
            pushHeap(lowerHalfMaxHeap, num);
        }
        else
        {
            // since push_heap() only supports max heap, simulate a min heap
            // with max heap by pushing the negated integer
            pushHeap(upperHalfMinHeap, -num);
        }

        // check for imbalance.
        if(lowerHalfMaxHeap.size() - 1 > upperHalfMinHeap.size())
        {
            // rebalance to correct imbalance by moving lower half max to upper half
            int lowerMax = popHeap(lowerHalfMaxHeap);
            pushHeap(upperHalfMinHeap, -lowerMax);
        }
        else if(upperHalfMinHeap.size() > lowerHalfMaxHeap.size())
        {
            // rebalance to correct imbalance by moving upper half min to lower half
            int upperMin = -popHeap(upperHalfMinHeap);
            pushHeap(lowerHalfMaxHeap, upperMin);
        }
    }

    /**
     * @brief Find the median of added integers.
     *
     * Finds & returns the median of integers added with addNum().  For an odd
     * no. of added integers this is the integer that equally partitions the integers.
     * For an even no. of integers this the average of 2 integer that equally
     * partitions the integers.
     *
     * @return The median of the added integers.
    */
    double findMedian() {
        if(size() % 2 == 0) {
            // case: even no. of added integers
            int lowerMedian = lowerHalfMaxHeap.front();
            // negate since ints stored in upper half min heap as a negative integer
            int upperMedian = -upperHalfMinHeap.front();

            return (upperMedian + lowerMedian) / 2.0;
        }

        // odd no. of added integers
        return lowerHalfMaxHeap.front();
    }

protected:
    /* @brief Returns the total no. of elements stored by this MedianFinder */
    size_t size()
    {
        return this->lowerHalfMaxHeap.size() + this->upperHalfMinHeap.size();
    }
};


/** @brief Tests MedianFinder using the test case.
 *
 * Tests MedianFinder using the test case of input nums and verifying the
 * actual output of MedianFinder with expected median passed.
 *
 * @param nums Vector of numbers added to the MedianFinder as test case input
 * @param expectedMedian The expected median value to check the actual median
 *                       given by MedianFinder against.
 * @throws runtime_error If the actual median is sufficiently close
 *                       to the expected median within the margin of error (+- 10^5)>
*/
void testMedianFinder(vector<int> nums, double expectedMedian)
{
    MedianFinder* medianFinder = new MedianFinder();
    for(int n: nums) {
        medianFinder->addNum(n);
    }

    double actualMedian = medianFinder->findMedian();
    // allowable margin of error: +-10^5
    if(abs(expectedMedian - actualMedian) > pow(10, -5))
    {
        ostringstream errMsg;
        errMsg << "Error: Median computed by median MedianFinder: " <<
            actualMedian <<
            " is not sufficiently close (+-10^5) to expected median: " <<
            expectedMedian;
        cerr << errMsg.str() << endl;
        throw new runtime_error(errMsg.str());
    }

    // cleanup resources
    delete  medianFinder;
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 */
int main()
{
    vector<int> testCase1 {72, 99, 23, 46, 21, 10};
    testMedianFinder(testCase1, (23+46) / 2.0);

    // seed the RNG to generate a deterministic test case
    srand(1);
    vector<int> testCase2(999);
    // init testCase2 to values: 0 -> 999
    iota(testCase2.begin(), testCase2.end(), 1);
    random_shuffle(testCase2.begin(), testCase2.end());
    testMedianFinder(testCase2, 500.0);

    vector<int> testCase3 {22};
    testMedianFinder(testCase3, 22.0);
}
