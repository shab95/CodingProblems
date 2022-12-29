
def length_of_longest_substring(arr, k):
    window_start = 0
    maxLength = 0
    zeroCount = 0
    for window_end in range(len(arr)):
        if arr[window_end] == 0:
            zeroCount += 1
        while (zeroCount > k):
            windowFirstDigit = arr[window_start]
            if windowFirstDigit == 0:
                zeroCount -= 1
            window_start += 1
        maxLength = max(maxLength, window_end - window_start + 1)

    return maxLength


'''
Summary:

The goal of this problem is to find the length of the longest subarray of 1s with k replacements. The first thing that came to my mind
was to physically replace the zeroes with ones and see what the longest possible subarray. However, this is not necessary. 

We can simply reword the problem by finding the longest subarray with 1s and max k zeroes. This solution applies the sliding window 
technique. We process each character one at a time. If the character is a zero, then we increase our count of the variable "zeroCount".
If the zeroCount ever exceeds k, then that means we have to shorten our window. We shorten our window by moving the window_start
up. If the window start is a zero and that decreases the zero count to equal or less than k, then we can continue extending the window.
However, if the window start element is a one, then we have to keep moving the start of the window forward until the zero count
goes below or equal to k. At every iteration, we can check the max length of the window by comparing the previous max length to
the current window size. In this program every window at the end of each iteration is valid.

Time Complexity: O(N) - The outer for loop and inner for loop each processes each element a maximum of one time. N + N -> O(N)
Space Complexity: O(1) - Constant space is used.

*Note*: The optimal solution uses an if statement instead of a while inside the for loop. This causes not every window to be valid.
        Check further reasoning for this online...
'''

print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
