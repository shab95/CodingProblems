from heapq import *


class MedianOfAStream:
    minHeapForBig = []  # add all big elements here
    maxHeapForSmall = []  # add all small elements here
    count = 0

    def insert_num(self, num):
        # if the max heap is empty or if the number is smaller than biggest num try entering there first
        # otherwise enter in
        if len(self.maxHeapForSmall) == 0 or -self.maxHeapForSmall[0] > num:
            heappush(self.maxHeapForSmall, -num)
        else:
            heappush(self.minHeapForBig, num)

        # if the length of the two heaps are not the same or max heap is not one larger(odd amount)
        # then correct balance
        if len(self.minHeapForBig) > len(self.maxHeapForSmall):
            switchSmallToMax = heappop(self.minHeapForBig)
            heappush(self.maxHeapForSmall, -switchSmallToMax)
        elif len(self.maxHeapForSmall) - 1 > len(self.minHeapForBig):
            switchBigToMin = heappop(self.maxHeapForSmall)
            heappush(self.minHeapForBig, -switchBigToMin)

        self.count += 1

    def find_median(self):
        # odd number, then look at the heap with the extra number(which is max heap)
        if self.count % 2 == 1:
            return -self.maxHeapForSmall[0]
        # even number case
        return (-self.maxHeapForSmall[0] + self.minHeapForBig[0])/2


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
