def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    
    while (left < right):
        currentSum = arr[left] + arr[right]
        if currentSum > target_sum:
            right -= 1
        elif currentSum < target_sum:
            left += 1
        else:
            return [left,right]
            
    return [-1,-1]


print(pair_with_targetsum([1,2,3,4,6],6))