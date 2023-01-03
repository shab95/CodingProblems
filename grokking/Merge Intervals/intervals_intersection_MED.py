'''
Problem Statement 
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''


# mycode
def merge(intervals_a, intervals_b):
    result = []

  # TODO: Write your code here
    start, end = 0, 0
    aPointer, bPointer = 0, 0

    while aPointer < len(intervals_a) and bPointer < len(intervals_b):
        aStart = intervals_a[aPointer][0]
        aEnd = intervals_a[aPointer][1]
        bStart = intervals_b[bPointer][0]
        bEnd = intervals_b[bPointer][1]

        aStartInBInterval = aStart >= bStart and aStart <= bEnd
        bStartInAInterval = bStart >= aStart and bStart <= aEnd

        if aStartInBInterval or bStartInAInterval:
            start = max(aStart, bStart)
            end = min(aEnd, bEnd)
            result.append([start, end])

        if bEnd < aEnd:
            bPointer += 1
        else:
            aPointer += 1
    return result


'''
Summary:

This problem can be solved using the merge intervals technique. It's very similar to the merge aspect of the merge sort.

In this problem, we are given two lists with ordered and disjoint intervals. This algorithm puts a pointer at the beginning of both
lists and traverses until each pointer reaches the end of the list. During each iteration, the intervals the pointers are at are 
compared for overlapping times. There 3 possible scenarios for each comparison. Let's name the two intervals being compared
A and B. A is coming from list 1 and B is coming from list 2.

Scenario 1: A and bBhave no intersecting times. In this case we want to do nothing and move forward the pointer of whichever interval
            has a smaller end time. We choose the smaller end time as there as a chance that the next interval in this respective list
            will intersect with the interval that had the bigger end time. (2 scenarios for A before B and before A)
            
Scenario 2: A envelops B or B envelops A. In these cases, the overlapping time is simply the interval being enveloped. The pointer
            with the enveloped list will have its pointer moving on.
            
Scenario 3: A is partly in B, but A ends later than B. B is partly in A, but B ends later than A. In these cases, the overlap is going
            to be between the interval with the later starting point and the interval with the earlier ending point. Whichever interval
            has an earlier ending point will have its pointer continue.

We do not have to worry about scenario 1 as there is no overlapping intervals. For scenarios 2 and 3, there are overlapping intervals.
They also have a method in common to get this overlapping interval. This is by getting the max of the starting points and min of the
ending points. This will give the overlapping interval. Now, we have to pick a pointer to move on. Whichever interval has an earlier
ending time will move on as there is a chance that the next interval in this respective list will have overlapping times with the
interval that had its pointer not move on(use examples). If both intervals have the same ending time, then it does not matter which
interval is moved forward.

Time Complexity: O(M + N) - We need traverse each list once.
Space Complexity: O(1) - Space will be needed with the output array, but the algorithm uses no extra space.
'''


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
