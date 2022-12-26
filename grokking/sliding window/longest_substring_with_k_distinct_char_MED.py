'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

# mycode


def longest_substring_with_k_distinct(str, k):
    window_start = 0
    longestSub = 0
    charFrequency = {}
    for window_end in range(len(str)):
        if str[window_end] not in charFrequency:
            charFrequency[str[window_end]] = 0
        charFrequency[str[window_end]] += 1

        while len(charFrequency) > k:
            charFrequency[str[window_start]] -= 1
            if charFrequency[str[window_start]] == 0:
                del charFrequency[str[window_start]]
            window_start += 1

        longestSub = max(window_end - window_start + 1, longestSub)
    return longestSub


'''
Summary:
Another sliding window problem. The window starts by adding the first character of the string. Characters are added to a hashmap
which counts the frequency of each character. The number of distinct characters is checked by the length of the hashmap. If the length
of the hashmap exceeds k, then characters from the beginning of the window are removed until the length of the hashmap(distinct count)
does not exceed k. The max length is always determined by getting the max of the current window length and the previous max length.

Time Complexity: O(N). The outer for loop reaches each character once. The inner while loop does not necessarily process every character
                        once, but the max number of times it can process each character is once. N+N -> O(N)
Space Complexity: O(K). Only keeping the distinct characters in the hashmap. Maybe plus one if we go over the distinct limit.
'''


def main():
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()


'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
Space Complexity 
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
'''
