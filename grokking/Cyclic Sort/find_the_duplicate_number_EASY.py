'''
Problem Statement 
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
'''

# mycode


def find_duplicate(nums):
    for i in range(len(nums)):
        ithElement = nums[i]

        while (nums[i] != i + 1):
            if nums[i] == nums[ithElement-1]:
                return nums[i]
            nums[i] = nums[ithElement - 1]
            nums[ithElement - 1] = ithElement
            ithElement = nums[i]

    return len(nums)


'''
Sumamry:
We can start this problem by applying the cyclic sort approach. The range of numbers given is between 1 and n, but there are 
n+1 characters. By using the cyclic sort, we try to put all the elements in the correct spot(1 goes to index 0, n goes to index
n-1).

Eventually, there will be a scenario where the duplicate numbers are swapping with each other to get into the same index. However,
this scenario also tells us what is the duplicate number. If we find two of the same numbers from different indexes trying to swap,
then we know that's our duplicate element.

Time Complexity: O(N) - Outer for loop processes each element once. Inner while loop does a maximum of N-1 swaps, so it is also O(N).
                        N + N-1 -> O(N)
Space Complexity: O(1) - No extra space is being used.
'''


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))
    print(find_duplicate([2, 2]))
    print(find_duplicate([1, 4, 2, 3, 6, 5, 1]))


main()
