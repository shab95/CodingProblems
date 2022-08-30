def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    
    closestSum = arr[0] + arr[1] + arr[2]
    
    for ind in range(len(arr)):
        left = ind + 1
        right = len(arr) - 1
        while (left < right):
            if arr[left] + arr[right] + arr[ind] == target_sum:
                return target_sum
            elif abs(target_sum - (arr[left] + arr[right] + arr[ind])) < abs(target_sum - closestSum):
                closestSum = arr[left] + arr[right] + arr[ind]
            elif ((abs(target_sum - (arr[left] + arr[right] + arr[ind])) == abs(target_sum - closestSum)) and ((arr[left] + arr[right] + arr[ind]) < closestSum)):
                closestSum = arr[left] + arr[right] + arr[ind]
            elif target_sum < (arr[left] + arr[right] + arr[ind]):
                right -= 1
            elif target_sum > (arr[left] + arr[right] + arr[ind]):
                left += 1
    return closestSum

print(triplet_sum_close_to_target([-2, 0, 1 ,2], 2))
print(triplet_sum_close_to_target([-3, -1, 1 ,2], 1))
print(triplet_sum_close_to_target([1, 0, 1 ,1], 100))