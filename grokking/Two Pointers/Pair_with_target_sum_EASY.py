def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            return [left, right]
        elif sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
    return -1


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
