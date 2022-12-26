'''
Problem Statement
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence.
This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
Write a function to sort the objects in -place on their creation sequence number in O(n) and without any extra space.
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.
Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
'''

# mycode


def cyclic_sort(nums):
    for i in range(len(nums)):
        while (nums[i] != i + 1):
            currentINum = nums[i]  # 3
            nums[i] = nums[nums[i] - 1]
            nums[currentINum - 1] = currentINum
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


'''
Summary:
Cyclic sort can only happen when certain rules are in place. In this case, the numbers in the list went from 1 to the length of the list.
In that case, we used a for loop to go to each element. When iterating through each element, if the element was not in the right spot,
we kept swapping with the element of where it's supposed to go(see example). Once we confirm the element is in the right spot,
we can iterate to the next element and do the same there. Once we reach the end of the list, the list will be sorted.

Time Complexity: O(N) - For loop is O(N), but there is also a while loop inside. The while loop will run a maximum of O(n-1) times for
                        n - 1 total swaps across all elements. Algorithm takes O(N) + O(N-1) -> O(N).
Space Complexity: O(1) - No extra space is used.
'''

# Example:
# 2,6,4,3,1,5
# Because we know the only entries are from 1 to n, then we can put the integer in the associated index. Example: "2" -> index 1
# 6,2,4,3,1,5
# Repeat until we find the correct number for that index
# 5,2,4,3,1,6
# 1,2,4,3,5,6
# Move past numbers with correct index. With this example from index 1 to index 3
# 1,2,4,3,5,6
# 1,2,3,4,5,6
# end once we check 6 is in the right place
main()
