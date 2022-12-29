def length_of_longest_substring(str, k):
    window_start = 0
    maxLength = 0
    focusLetter = ''
    charCount = [0] * 26
    for window_end in range(len(str)):
        currentChar = str[window_end]
        currentOrd = ord(currentChar)
        charCount[currentOrd - ord('a')] += 1
        if focusLetter == '':
            focusLetter = currentChar
        elif charCount[currentOrd - ord('a')] >= charCount[ord(focusLetter) - ord('a')]:
            focusLetter = currentChar
        while (window_end - window_start + 1 - charCount[ord(focusLetter) - ord('a')] > k):
            startWindowChar = str[window_start]
            charCount[ord(startWindowChar) - ord('a')] -= 1
            focusLetter = chr(charCount.index(max(charCount)) + ord('a'))
            window_start += 1
        maxLength = max(maxLength, window_end - window_start + 1)
    return maxLength

# answer


# def length_of_longest_substring(str, k):
#     window_start, max_length, max_repeat_letter_count = 0, 0, 0
#     frequency_map = {}

#     # Try to extend the range [window_start, window_end]
#     for window_end in range(len(str)):
#         right_char = str[window_end]
#         if right_char not in frequency_map:
#             frequency_map[right_char] = 0
#         frequency_map[right_char] += 1
#         max_repeat_letter_count = max(
#             max_repeat_letter_count, frequency_map[right_char])

#         # Current window size is from window_start to window_end, overall we have a letter which is
#         # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
#         # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
#         # if the remaining letters are more than 'k', it is the time to shrink the window as we
#         # are not allowed to replace more than 'k' letters
#         if (window_end - window_start + 1 - max_repeat_letter_count) > k:
#             left_char = str[window_start]
#             frequency_map[left_char] -= 1
#             window_start += 1
#         print(window_start, window_end)
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length
'''
Summary (My solution):

This solution works by using the sliding window technique. The longest substring we can make is such that the end of the window - the
beginning of the window + 1 minus the count of the most frequent character in that substring is larger than k. 

We can do this by storing the frequency of each character in a hashmap/array. Now, we also have to keep track of the highest frequency 
character. If the length of the substring - the most frequenct character is greater than k, then that means there are characters in
the substring that we can't use our replacements on. When this happens, we decrease the size of the window. We do this by
moving the window_start variable forward. After moving this variable forward, we have to grab our new highest frequent character count.
We do this in the case that moving the variable forward actually makes the current highest count character the second highest count
character. For every iteration, we keep track of the max substring length by comparing the previous max substring length to the 
current window size.

Time Complexity: O(N) - Outer for loop processes each character once. The inner while loop processes each character a maximum of 
                        one time.
Space Complexity: O(1) - We keep constant space by using an array instead of a hashmap. We only need 26 entries at all times.
'''
# print(length_of_longest_substring("aabccbb", 2))
# print(length_of_longest_substring("abbcb", 1))
# print(length_of_longest_substring("abccde", 1))
print(length_of_longest_substring("aaabcc", 2))
