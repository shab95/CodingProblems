def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    closestSum = arr[0] + arr[1] + arr[2]
    closestTriplet = [arr[0], arr[1], arr[2]]
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[left] + arr[right] + arr[i]
            if abs(target_sum - currentSum) < abs(target_sum - closestSum) or abs(target_sum - currentSum) == abs(target_sum - closestSum) and currentSum < closestSum:
                closestSum = currentSum
                closestTriplet = [arr[i], arr[left], arr[right]]

            if target_sum - currentSum < 0:
                right -= 1
            elif target_sum - currentSum > 0:
                left += 1
            else:
                closestSum = target_sum
                closestTriplet = [arr[i], arr[left], arr[right]]
                return closestSum
    return closestTriplet


'''
Summary:

To solve this problem, we can use the two pointers technique. First, we keep a record of a closestSum. We can do this by just taking
the sum of the first three integers. This gives a basis to compare the other sums. 

We start the algorithm by sorting the array. This helps in avoiding duplicates and also increases the speed of finding the closest sum.
We also set a clause to avoid finding duplicate triplets early in the for loop. For each element we iterate through in the outer for 
loop, we try to find a closest triplet. We do this by setting a left pointer to the index right of the element we're looking at 
in the for loop. The right pointer will always be the last element in the array. 

We increase the left pointer if the difference between the target sum and current sum is positive(current sum is too small). We decrease
the right pointer if the difference is negative(current sum is too big). If the difference is zero, then it means we have found a
triplet that equals the target sum and we can end the algorithm. The problem also states a condition that if two triplets have
the same distance from the target sum, then we choose the triplet with the smaller sum. We set this condition in the first if statement
of the while loop.

Time Complexity: O(N^2) - Sorting takes NlogN time. The outside for loop takes N time. The while loop takes N time and happens for each
                          iteration in the for loop. NlogN + N * N -> O(N^2)
Space Complexity: O(N) - Python uses Tim sort which uses O(N) space. The algorithm itself does not use any extra space.
'''

print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
