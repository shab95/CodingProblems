def search_triplets(arr):
    arr.sort()
    triplets = []
    
    for ind in range(len(arr)):
        if arr[ind] == arr[ind - 1]:
            continue
        left,right = ind + 1, len(arr) -1 
        targetSum = -1 * arr[ind]
        while left < right:
            if arr[left] == arr[left -1]:
                left += 1
            elif (right + 1 < len(arr)) and (arr[right] == arr[right + 1]):
                right -= 1
                
            currSum = arr[left] + arr[right]
            if currSum == targetSum:
                    triplets.append([arr[ind],arr[left],arr[right]])
                    left += 1
                    right -= 1
            elif currSum > targetSum:
                right -= 1
            elif currSum < targetSum:
                left += 1
    return triplets

print(search_triplets([-3,0,1,2,-1,1,-2]))
print(search_triplets([-5,2,-1,-2,3]))
                     
            
                 