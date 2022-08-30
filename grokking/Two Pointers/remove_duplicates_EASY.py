def remove_duplicates(arr):
    if len(arr) == 1:
        return 1

    nextNonDuplicate = 1
    next = 1
    
    while next < len(arr):
        if arr[next] != arr[nextNonDuplicate - 1]:
            arr[nextNonDuplicate] = arr[next]
            nextNonDuplicate += 1
        next += 1
    
    print(arr)
    return nextNonDuplicate

print(remove_duplicates([2,2,2,11]))

def remove_key(arr, key):
    if len(arr) == 1:
        return 1
    
    nextNonKey = 0
    next = 0
    
    while next < len(arr):
        if arr[next] != key:
            arr[nextNonKey] = arr[next]
            nextNonKey += 1
        next += 1
    print(arr)
    return nextNonKey + 1


print(remove_key([3,2,3,6,3,10,9,3],3))

print(remove_key([2,11,2,2,1],2))