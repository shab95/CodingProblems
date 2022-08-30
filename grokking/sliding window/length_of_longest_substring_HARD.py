def length_of_longest_substring(str,k):
    window_start = 0
    maxLen = 0
    charHM = {}
    maxRepeatingCharater = 0
    for window_end in range(len(str)):
        endWinChar = str[window_end]
        if endWinChar not in charHM:
            charHM[endWinChar] = 0
        charHM[endWinChar] += 1
        maxRepeatingCharater = max(maxRepeatingCharater,charHM[endWinChar])
        
        if (window_end - window_start + 1 - maxRepeatingCharater > k):
            startWinCh = str[window_start] 
            charHM[startWinCh] -= 1
            window_start += 1
        
        maxLen = max(maxLen, window_end - window_start + 1)
    return maxLen

print(length_of_longest_substring("aabccbb",2))
print(length_of_longest_substring("abbcb",1))
print(length_of_longest_substring("abccde",1))
