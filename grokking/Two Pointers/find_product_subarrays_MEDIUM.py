from collections import deque

def find_subarrays(arr, target):
    result = []
    left = 0
    
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while (product > target and left < len(arr)):
            product /= arr[left]
            left += 1
        
        tempArr = deque()
        for i in range(right, left - 1, -1):
            tempArr.appendleft(arr[i])
            result.append(list(tempArr))
            print(tempArr)
        print(result)
    return result

print(find_subarrays([2,5,3,10],30))
print()
print()
print(find_subarrays([8,2,6,5],50))
        