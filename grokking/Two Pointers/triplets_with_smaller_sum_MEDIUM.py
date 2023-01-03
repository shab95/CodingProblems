def triplet_with_smaller_sum(arr, target):
    count = 0
    triplets = []
    arr.sort()

    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            currentSum = arr[left] + arr[right] + arr[i]
            if currentSum < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


'''
Summary:

This problem can be solved using the two pointers technique. First, we sort the list as it makes the process of finding smaller sums
simpler. 

The outer for loop traverses through the entire list. For each iteration, the left pointer is set right after the current element
we are looking at. This helps avoid duplicate counts of the same triplets. The right pointer is always set to the end of the list.
If at any point we find a sum that is less than the target, then we can increase count. The trick in this problem is increasing
the count by right - left. We can also include all the numbers between left or right as we know if the current right pointer
produces a sum less than target. If we set the right pointer to the numbers between left or right, then we would also get a sum
less than target. This is because the list is sorted and we know that any number at a index before the right pointer is smaller
than the right pointer.

However, if the sum is greater than target, then we can decrease the right pointer by 1 index as we need a smaller sum.

Time Complexity: O(N^2) - Sorting the list takes NlogN time. The outer for loop processes each element, so N time. The while loop
                          takes N time for each iteration. This makes the whole for loop an N^2 operation. N + N -> N^2
Space Complexity: O(N) - Python uses Tim Sort which uses N space. The actual algorithm uses no extra space.
'''
print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
