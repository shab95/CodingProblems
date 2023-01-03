'''

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''

# mycode
from __future__ import print_function


class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end
    for x in range(len(intervals)):
        currentInterval = intervals[x]
        if currentInterval.start <= end:
            end = max(currentInterval.end, end)
        else:
            mergedIntervals.append(interval(start, end))
            start = currentInterval.start
            end = currentInterval.end
    mergedIntervals.append(interval(start, end))
    return mergedIntervals


'''
Summary:

This algorithm uses the merge intervals technique(name of the problem too). 

First, we sort the intervals by the start of each interval as this makes the process of merging intervals much simpler.

There are 4 possibilities between two interval. Let's name interval 1 A and interval 2 B. The first possibility is A.end < B.start.
In this case, the intervals does not to be merged. Second, A.start = B.start and A.end < B.end. In this case, the interval just
needs to be the B interval. Third, A.start < B.start and B.end < A.end. In this case, the interval just need to be the A interval.
Last, B.start < A.end and B.end > A.end.

This algorithm accounts for all scenarios. Essentially, it uses a start and end variable to constantly keep track of the current
merged interval(in case there are multiple intervals being merged into one). The start interval is initially set to the start
of the first interval and the same goes for the end interval. We start a for loop at the second interval since we already know
and stored the first interval. 

If the interval currently being examined by the for loop has a start value that is lower or equal to what is stored in the end variable, 
then that means the intervals can be merged. The problem is finding the bigger end value now. We want the bigger end value, which
will cover more value, so we take the maximum of the end variable and the current interval's end value. 

If the interval currently being examined by the for loop has a start value that's greater than the value stored in end, that means
the two intervals do not overlap. This means we can create an interval using the values stored in the start and end variable. We can
add this interval to the merged intervals list because we know all values coming later in the given intervals list can not be overlapped
with intervals that are in the merged intervals list.

Finally, after the for lop ends we need to add the final interval using the stored values in start and end.

Time Complexity: O(NlogN) - Although the algorithm only has one for loop that goes through each value once, sorting takes NlogN time.
Space Complexity: O(N) - We return a list that can be max N size. The algorithm itself does not itself use space, but the sorting does.
'''


def main():
    print("Merged intervals: ", end='')
    for i in merge([interval(1, 4), interval(2, 5), interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([interval(6, 7), interval(2, 4), interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([interval(1, 4), interval(2, 6), interval(3, 5)]):
        i.print_interval()
    print()


main()
