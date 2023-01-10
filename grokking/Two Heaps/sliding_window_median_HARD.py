'''
Problem Statement 
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0

Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
'''


# mycode
import heapq
from heapq import *


# answer


class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []
        self.hash = {}
        self.balance = 0

    def find_sliding_window_median(self, nums, k):
        # first split the first k among heaps
        for i in range(k):
            heappush(self.maxHeap, -1 * nums[i])
        for i in range(int(k/2)):
            heappush(self.minHeap, -1 * heappop(self.maxHeap))

        # start sliding window
        window_start = 0
        medians = []
        for window_end in range(k, len(nums)):
            medians.append(self.find_median(k))

            # checking the balance of valid elements
            outgoingNum = nums[window_start]
            incomingNum = nums[window_end]
            self.balance = 0
            if outgoingNum not in self.hash:
                self.hash[outgoingNum] = 0
            self.hash[outgoingNum] += 1

            if outgoingNum <= -1 * self.maxHeap[0]:
                self.balance -= 1
            else:
                self.balance += 1

            if incomingNum <= -1 * self.maxHeap[0]:
                self.balance += 1
                heappush(self.maxHeap, -1 * incomingNum)
            else:
                self.balance -= 1
                heappush(self.minHeap, incomingNum)

            self.balance_heaps()
            #print(self.hash, window_end, window_start, outgoingNum)
            self.removeInvalids()
            window_start += 1

        medians.append(self.find_median(k))
        return medians

    def balance_heaps(self):
        if self.balance < 0:
            heappush(self.maxHeap, -1 * heappop(self.minHeap))
        elif self.balance > 0:
            heappush(self.minHeap, -1 * heappop(self.maxHeap))

    def removeInvalids(self):
        while len(self.maxHeap) > 0 and -1 * self.maxHeap[0] in self.hash:
            self.hash[-1 * self.maxHeap[0]] -= 1
            if self.hash[-1 * self.maxHeap[0]] == 0:
                del self.hash[-1 * self.maxHeap[0]]
            heappop(self.maxHeap)

        while len(self.minHeap) > 0 and self.minHeap[0] in self.hash:
            self.hash[self.minHeap[0]] -= 1
            if self.hash[self.minHeap[0]] == 0:
                del self.hash[self.minHeap[0]]
            heappop(self.minHeap)

    def find_median(self, k):
        print('finding mean', self.maxHeap, self.minHeap)
        if k % 2 == 0:
            return float(-1 * self.maxHeap[0] + self.minHeap[0])/2
        return -1 * self.maxHeap[0]


'''
Solution:

This problem needs to be redone a couple more times for a more thorough understanding, but here is an attempt at a written solution.
This problem can be solved with two heaps with lazy removal.

Essentially, we use two heaps. One with the bigger half of the numbers in the window, this is our min heap. The other has the smaller
half of the numbers in the window, this is our max heap. In python, the heapq library doesn't actually have a max heap, but a min heap
can be treated as a max heap if numbers are negated when inserted and accessed. If our k is an even number that means both heaps will
have the same number of elements and the average of the biggest in the minheap and smallest in the maxheap will be our median. If k
is odd, then the heap with more elements will have the median(either the biggest in the minheap and smallest in the maxheap). In this
code, we automatically put the extra element in the max heap. This is why we return the biggest in the max heap when we want to find the
median if k is odd(find_median function).

There are some problems we have to address when we use this solution. The first is adding numbers and keeping the number of elements
in both heaps balanced as that is the only way the top of both heaps can help in finding the median. We do this by creating a balance
heaps function. We initially set both heaps to k/2 elements(ceil(k/2) in the max heap if k is odd). This sets our basis for creating
even sized heaps. Now, when we are moving the window forward, we want add the new element. The new element can be added by simply 
checking whether the new element is less than or equal to the maximum in the max heap. If it does fit that conditional, then the
number can go in max heap. Otherwise, the number will go into min heap. This solves the problem for adding elements. 

Our next problem is removing elements. When we move our window up, we will want to discard elements that are not in the window anymore.
The main issue with literally discarding elements is that, it would take take N time to heapify after removal. Instead we should focus
on the elements still in the window. The main understanding is that if there are an equal number of elements within the window in both
heaps(or 1 more in max heap if k is odd) and both the biggest in the max heap and smallest in the min heap are also valid, then the
median we calculate is valid. Use examples. 

Our first step is that there is an even number of valid(in the window) elements within each heap. We can do this by checking if
the heaps are balanced or imbalanced with the incoming and outgoing elements. When the window moves, we both add and "remove" an element.
If the addition and removal is done on the same heap, then the number of valid elements is still balanced. However, if one heap is doing
the removal and the other is doing the addition, then we must ensure that the heap that is doing the addition transfers a valid element
to the one that does the removal to maintain balance of valid elements. This can be simply done by taking the biggest in the max heap
and moving it to min heap or vice versa. Now, each heap has the same valid elements(or k/2 + 1 in max heap if k is odd). Pushing an
element into the heap is a logK transaction.

However, doing the transfer of valid elements to keep balance can create another problem. That problem is that the biggest of the max
heap and the smallest in the min heap become invalid elements. However, if elements are invalid and on top of the heaps, then we only
spend logk. The issue now is knowing which elements are invalid. To solve this problem we can use a hashmap to keep track of all the
invalid elements. These are elements that are leaving the sliding window. At max, there should be n-k invalid elements. Once we remove
all the invalid elements that appear at the top of each heap we are still left with heaps that have an equal number of valid elements
in each and the median we calculate will be accurate as well.

Time Complexity: O(NlogK) - Inserting elements into heap is logK time. We will end up inserting each element at least once. Some even
                            twice because of transfers. The removal of invalid elements also takes O(logK) time. There should be a max
                            of N-K invalid elements. Hashmap access is O(1). N * logK + (N-k) * logK + 1 -> NlogK
Space Complexity: O(N) - The heaps require O(K) space in total, but they can also store invalid elements. The hash table will also store
                         up to N-K invalid elements. N + N - K -> N
'''


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
