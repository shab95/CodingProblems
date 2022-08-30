def length_of_longest_substring_binary(arr,k):
    window_start = 0
    maxLen = 0
    freqOne = 0
    
    for window_end in range(len(arr)):
        endWinNum = arr[window_end]
        if endWinNum == 1:
            freqOne += 1
        
        while (window_end - window_start + 1 - freqOne > k):
            startWinNum = arr[window_start]
            if startWinNum == 1:
                freqOne -= 1
            window_start += 1
        maxLen = max(maxLen,window_end - window_start + 1)
        
    return maxLen

print(length_of_longest_substring_binary([0,1,1,0,0,0,1,1,0,1,1],2))
print(length_of_longest_substring_binary([0,1,0,0,1,1,0,1,1,0,0,1,1],3))