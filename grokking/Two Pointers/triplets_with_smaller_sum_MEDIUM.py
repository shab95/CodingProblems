def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    for ind in range(len(arr)):
        if arr[ind] == arr[ind - 1]:
            continue
        left, right = ind + 1, len(arr) -1 
        while (left < right):
            if (arr[ind] + arr[left] + arr[right] < target):
                count += (right - left)
                left += 1
            else:
                right -= 1
    return count


print(triplet_with_smaller_sum([-1,0,2,3],3))
print(triplet_with_smaller_sum([-1,4,2,1,3],5))