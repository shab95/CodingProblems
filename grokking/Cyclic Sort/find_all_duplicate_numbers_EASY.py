'''
Problem Statement 
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
'''


def find_all_duplicates(nums):
    for i in range(len(nums)):
        ithElement = nums[i]

        while i + 1 != ithElement and ithElement != nums[ithElement - 1]:
            nums[i] = nums[ithElement - 1]
            nums[ithElement - 1] = ithElement
            ithElement = nums[i]

    duplicateElements = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateElements.append(nums[i])

    return duplicateElements


'''
Summary:
This problem can be solved cyclic sort. Cyclic sort because we know the numbers are in the range of 1 to n and there are only n elements
in the list. For this problem, we put every element in the correct index. Because we know every element is exactly 1 more than the index,
we can do this check. However, in the case we are swapping the duplicate number with itself, we skip this case. 

After putting all the numbers except the duplicates in the right place, we go through the list once and see which numbers are out of 
place. 

Time Complexity: O(N) - The for loop is going to process each character once. The while loop will also do a maximum of N-1 swap.s
                        N + N -> O(N)
Space Complexity: O(1) - No extra space is used.
'''


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
