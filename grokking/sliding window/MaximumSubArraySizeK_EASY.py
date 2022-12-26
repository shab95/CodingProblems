import math


def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if ((window_end - window_start + 1) == k):
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


'''

Summary:
The max sub array of a list size k with positive integers. Start by getting the sum of the first k digits. Since this is the first
sum, we set the max sum variable to this sum. Also, this creates a window of the first k digits. To test all windows, we can add the
next element to our window and remove the first element from the current window. This way we still have a window that is of size k.
Every time the window's sum is more than the max, we change the max sum.
Time: O(N) since we hit each element once
Space: O(1)
  
'''


def main():
    print("Maximum sum of a subarray size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
