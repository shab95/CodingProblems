'''
Problem Statement 
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
'''

# mycode
from heapq import *


class MedianOfAStream:
    minHeap = []
    maxHeap = []

    def insert_num(self, num):
        if len(self.maxHeap) == 0 or num <= -1 * self.maxHeap[0]:
            heappush(self.maxHeap, -1 * num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            biggestInMax = -1 * heappop(self.maxHeap)
            heappush(self.minHeap, biggestInMax)
        elif len(self.minHeap) > len(self.maxHeap):
            smallestInMin = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * smallestInMin)

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            smallestOverMed = self.minHeap[0]
            biggestUnderMed = -1 * self.maxHeap[0]
            return float(smallestOverMed + biggestUnderMed)/2

        return -1 * self.maxHeap[0]


'''
Summary:

This problem can be solved with heap sort and a byproduct of heapsort, which are min heaps and max heaps. Since the goal is to find the
median, then we can create two lists. The first list will contain all numbers smaller than the median with the biggest number being
available to us(max heap). The second list will contain all numbers bigger than the median with the smallest number being available
to us(min heap). If each list contains approximately half the elements of the list, then there can be two scenarios. If there are
an odd amount of elements, then one of the lists will have more elements. If the bigger than median list has more elements, then
we know the smallest element in that list is the median. If the smaller than median list has more elements, then we know the biggest
element in that list is the median. If there are an even number of elements, then we can take an average between the biggest of the
list with the smaller numbers and the smallest of the list with the bigger numbers.

We can create this two lists using the heapq library provided by Python. Our two functions are going to be insert_num and find_median.
Before we understand the code, we can prematurely make the decision that if there are an odd amount of elements, then the extra element
will always be found in the max heap. The min heap will also work if you want to put the extra element there. To insert numbers, there
are two stages. First, putting numbers in either heap. Second, leveling it out so both heaps have the same amount of digits or the max
heap has one more digit. In this code, we always add to minheap unless the maxheap is empty or the number we are adding is less than
the biggest in max heap. For the second step, we just check the list size is either equal or the max heap is one bigger. If either of
those scenarios are not true, then we take an element from the bigger heap and place it in the smaller heap.

To find the median, there are also two scenarios. If both heaps are of equal length that means there are an even number of elements and
we can take the average of the smallest in minheap and biggest in maxheap. However, if the length is uneven(odd number of elements), then
we can take the biggest in maxheap, since we made the algorithm always place the extra digit in max heap.

***NOTE***
Python does not have a max heap inherently. The heapq library only provides min heaps. To turn a min heap into a max heap, we can just
negate the number when pushing it in. When pulling the number out, we also negate it to get the number we inserted back. 

Time Complexity: O(logN) - Inserting a number in a heap takes logN time. Finding the median takes constant time.
Space Complexity: O(N) - We store all the numbers in the stream.

'''


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
