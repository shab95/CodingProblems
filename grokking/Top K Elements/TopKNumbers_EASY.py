from heapq import *


# 1) Put the first K elements into the heap, so we have a base set of numbers
# 2) Check that there are at least K elements in the list
# 3) Go through the rest of the elements. If we find an element bigger than the smallest one in the heap, then replace the
# smallest one with the bigger element found.
def findKLargestNumber(lst, k):
    minHeap = []
    for i in range(len(k)):
        if lst[k]:
            heappush(minHeap, k)
        else:
            return minHeap

    for i in range(k + 1, len(k)):
        minElement = minHeap[0]

        if minElement < lst[i]:
            heappop(minHeap)
            heappush(minHeap, lst[i])
    return list(minHeap)
