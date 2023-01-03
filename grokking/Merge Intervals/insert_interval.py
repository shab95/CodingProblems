'''
Problem Statement 
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
'''


def insert(intervals, new_interval):
    merged = []
    # TODO: Write your code here
    if len(intervals) < 1:
        return [new_interval]

    start = intervals[0][0]
    end = intervals[0][1]
    inserted = False
    for currentInterval in intervals:
        if currentInterval[0] <= end:
            end = max(end, currentInterval[1])
        else:
            merged.append([start, end])
            start = currentInterval[0]
            end = currentInterval[1]

        if not inserted:
            if new_interval[0] < start and new_interval[1] < start:
                merged.append(new_interval)
                inserted = True
            elif new_interval[0] <= end:
                start = min(start, new_interval[0])
                end = max(end, new_interval[1])
                inserted = True
    merged.append([start, end])
    if not inserted:
        merged.append(new_interval)
    return merged


'''
Summary:

This problem can be solved using the merge intervals technique. Essentially, it is the same problem, but we must add another interval
into the mix. 

We create a boolean inserted variable to check whether the interval has been inserted into the merged list avoid duplicating its entry.
The way we know how to insert the new interval is by checking if the new interval's start value is less than the current end value.
If the start value is less than the end value, then that means there is an overlap. In this case, we need to merge these intervals.
To do this, we set the start variable to the minimum of the current interval and the new interval's start. We also set the end variable
to the maximum of the current interval and the new interval's max. We finally add this interval to the merged list once we run
out of seeing intervals that overlap with that start and end variable.

There is an edge case where the new interval falls perfectly in between two intervals. This is why we check if the new interval's start
and end times are before another interval's start time. If it is, then we just add the new interval to the merged list as is.

Once the for loop ends, in case the new interval has not been added yet, we also add it as is.

Time Complexity: O(N) - Sorting not needed here. We also only use one for loop to process all intervals.
Space Complexity: O(N) - No extra space is used in the algorithm, but the returning list is always going to be size N + 1.

***NOTE***
An alternative way to find out where to enter the new interval is to see when the new interval's start time becomes less than
the previous interval's end time.

The initial problem also doesn't state we have to merge intervals that don't overlap with the new interval.

This is why this answer can be used:

'''
# Grokking Soln.
# answer

# def insert(intervals, new_interval):
#     merged = []
#     i, start, end = 0, 0, 1

#     # skip (and add to output) all intervals that come before the 'new_interval'
#     while i < len(intervals) and intervals[i][end] < new_interval[start]:
#         merged.append(intervals[i])
#         i += 1

#     # merge all intervals that overlap with 'new_interval'
#     while i < len(intervals) and intervals[i][start] <= new_interval[end]:
#         new_interval[start] = min(intervals[i][start], new_interval[start])
#         new_interval[end] = max(intervals[i][end], new_interval[end])
#         i += 1

#     # insert the new_interval
#     merged.append(new_interval)

#     # add all the remaining intervals to the output
#     while i < len(intervals):
#         merged.append(intervals[i])
#         i += 1
#     return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))

    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [6, 7]], [4, 5])))


main()
