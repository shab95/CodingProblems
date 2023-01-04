# Problem Statement
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Appointments: [[1, 4], [2, 5], [7, 9]]
# Output: false
# Explanation: Since[1, 4] and [2, 5] overlap, a person cannot attend both of these appointments.

# Example 2:

# Appointments: [[6, 7], [2, 4], [8, 12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.

# Example 3:

# Appointments: [[4, 5], [2, 3], [3, 6]]
# Output: false
# Explanation: Since[4, 5] and [3, 6] overlap, a person cannot attend both of these appointments.

# mycode


def can_attend_all_appointments(intervals):
    # TODO: Write your code here
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        currIntervalStart = intervals[i][0]
        prevIntervalEnd = intervals[i-1][1]
        if currIntervalStart < prevIntervalEnd:
            return False
    return True


'''
Summary:

This problem can be solved by thinking of the intervals as merging intervals. Checking if any intervals merge is the goal of the problem.
Checking if any interval merges with another would take too long if we used nexted for loops. A simpler way is to sort the intervals
based on the starting time. Next, we iterate this list starting at the second interval and check if any of the current interval's start
times are less than the previous interval's end time. If this is the case, then there is an overlap and we can return false. If this
condition is never reached, then that means there are no overlaps and we can return True.

Time Complexity: O(NlogN) - Sorting takes NlogN time, but outside of that there is only one for loop, which is N.
Space Complexity: O(N) - Sorting in Python used N space(Tim Sort), but the algorithm itself or the output does not use extra space.
'''


def main():
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
