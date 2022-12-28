def non_repeat_substring(str):
    window_start = 0
    longestSub = 0
    charArr = [0] * 26

    for window_end in range(len(str)):
        char = str[window_end]
        charArr[ord(char) - ord('a')] += 1
        while charArr[ord(char) - ord('a')] > 1:
            firstWinChar = str[window_start]
            charArr[ord(firstWinChar) - ord('a')] -= 1
            window_start += 1

        longestSub = max(longestSub, window_end - window_start + 1)
    return longestSub


'''
Summary:
The basis of this problem is to find the longest substring of characters with no repeats.

This problem requires the sliding window technique. We go through each character once. Also, we have an array of length 26 which
has one index for each letter of the alphabet. Each index represents a binary check if we have seen the character or not. If we
have seen the character, then we move our window up. This means we take a look at our first character in the window(represented by
window_start) and start removing them until the character we just added only has one occurrence in our window. 

At the end of each iteration of the outer for loop, we can check if our substring is the biggest one we have seen so far. This can be
done by comparing the previous longest substring to length of the window(window_end - window_start + 1).

Time Complexity: O(N) - The outside for loop is going to reach every character once. The inner while loop while process each character
                        a maximum of one time. N + N -> O(N)
Space Complexity: O(1) - Constant space is needed(array of length 26) and it is not dependent on N.
'''

'''
Alternative Solution:

The major issue we see in this problem is what we do when we see a character for the second time. One way to counter this issue is
by using a hashmap that tracks the last time we have seen each character. If our window_start variable is past the last time we 
have seen each character, then we can add that character to the current window. if the window_start variable is before the last
time we have seen the first occurence of the character, then we have to move the window_start one space past the first occurence
of the character. With each iteration, we can check for the max substring. This would remove the while loop, but also introduce a hash
map.

Technically, the hashmap would make the space complexity O(N), but an array of length 26 could also be used. This would make
the space complexity O(1) again.
'''
print(non_repeat_substring("aabccbb"))
print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))
