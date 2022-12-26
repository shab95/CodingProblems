import math
'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

# mycode


def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    window_sum = 0
    smallestSubarray = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while (window_sum >= s):
            smallestSubarray = min(
                window_end - window_start + 1, smallestSubarray)
            window_sum -= arr[window_start]
            window_start += 1
    return smallestSubarray


'''
Summary:
Sum elements in the array starting from the beginning until the sum is greater than or equal to S. Once the sum is greater than S, 
set the smallest subarray variable to the current length of all the elements you have added up. All the elements summed so far is the
"window" we are working with. Remove the elements from the beginning of the window and check if the sum remains greater than or equal
to S. If the sum is still greater than S, then change the smallest subarray variable accordingly. Once enough elements have been removed
to make the sum less than S, add more elements that have yet to be seen. Repeat this process until the window reaches the end.
'''


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
