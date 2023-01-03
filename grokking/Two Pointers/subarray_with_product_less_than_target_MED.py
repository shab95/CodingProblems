'''
Problem Statement 
Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''

# mycode
from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1
    window_start = 0

    for window_end in range(len(arr)):
        product *= arr[window_end]

        while product >= target and window_start < len(arr):
            product /= arr[window_start]
            window_start += 1

        subarray = deque()
        for x in range(window_end, window_start - 1, -1):
            subarray.appendleft(arr[x])
            result.append(list(subarray))
    return result


'''
Summary:

This problem is classified as a two pointers problem, but it makes more sense to approach it as a sliding window problem. Every sliding
window problem is basically a two pointers problem since we need to keep track of the starting and ending point.

As a sliding window problem goes, we keep track of the start of the window and the end of the window. The for loop keeps extending
the end of the window with each iteration. We can shorten the window by increasing the start of the window. The only time we would
need to do this is if the running product is greater than or equal to the target. In that case, we start dividing away numbers
at the beginning of the window.

The tricky part to this problem is actually getting all unique subarrays. It's better to try out with examples why the following
reasoning works. The reason we add the digits from right to left is so we avoid getting duplicates. Since we are already traversing
the list from left to right we will already have subarrays for the first parts of the window. If we created the subarrays going from
the left part of the window to the right part of the window, we would be creating duplicate subarrays and we would not end up getting
all the subarrays as well. To fix this, we add subarrays from right to left. This way we avoid getting the duplicate subarrays that
form at the beginning of the window. Also, the element we just added to the window will properly be included in every subarray as well.

The reason to use deques during this process is to use the appendleft method. With normal lists, appending to the beginning of the list
is difficult.

Time Complexity: O(N^2) - The outer for loop processes each element once. Creating subarrays processes is an N operation. Increasing the
                          window can happen a maximum of N times. N * N + N -> O(N^2)
Space Complexity: O(N) - The only time the algorithm uses space is when adding subarrays to the result. The maximum size of the subarray
                         list is going to be O(N). The output, however, can be O(N^2) size. The worst case is the product of the entire
                         list being less than the target. In this case, the output's size would be 1 + 2 + ... + n. Why? At index 0,
                         we can create one subarray. At index 1, we can create two subarrays. At the last index, we can create n
                         subarrays. 1 + 2 + ... + n = (n+1) * n/2 -> O(N^2). Output will take O(N^2) space.
'''


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
