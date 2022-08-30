def non_repeat_substring(str):
    window_start = 0
    maxStrLen = 0
    strHM = {}
    for window_end in range(len(str)):
        curChar = str[window_end]
        if curChar not in strHM:
            strHM[curChar] = 0
        strHM[curChar] += 1
    
        while (strHM[curChar] > 1):
            startWinChar = str[window_start]
            strHM[startWinChar] -= 1
            if strHM[startWinChar] == 0:
                del strHM[startWinChar]
            window_start += 1
        maxStrLen = max(maxStrLen, window_end - window_start + 1)
        
    return maxStrLen
print(non_repeat_substring("aabccbb"))
print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))