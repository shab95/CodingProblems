'''
Problem Statement 
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:

Input: [2, 4, 1, 2]
Output: 3

Example 3:

Input: [2, 3, 2, 1]
Output: 4
'''


# mycode
def find_missing_numbers(nums):
    missingNumbers = []
    # TODO: Write your code here
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if i != j and j != nums[j] - 1:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if i != nums[i]-1:
            missingNumbers.append(i+1)
    return missingNumbers


'''
Be careful about i != j and nums[i] != nums[j]
when there are duplicates in index i, then using i!=j as condition, while will keep looping
using nums[i] != nums[j] can avoid this problem, because duplicates means there exists nums[i] = nums[j]

2 4 1 2

i=0
4 2 1 2
2 2 1 4
i=1
2 2 1 4
i=2
1 2 2 4
i=3
1 2 2 4
'''


# mycode2
def find_missing_numbers(nums):
    for i in range(len(nums)):
        ithElement = nums[i]

        while (ithElement != i + 1 and nums[i] != nums[nums[i] - 1]):
            # swap
            nums[i] = nums[nums[i] - 1]
            nums[ithElement - 1] = ithElement
            ithElement = nums[i]
    missingNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers


'''
Summary:
The problem we are trying to solve is finding the missing numbers. In this case, there are duplicate numbers that cover up where
the missing numbers are going to be. Also, the range of numbers in this list is from 1 to n, so there are no extra digits that
do not fit into the range. 

The basic idea is to run the cyclic sort and put all the numbers in positions they are supposed to be in. The edge case in this 
scenario is what is going to happen when you have two numbers that should go into the same place. Normally, this would make the 
cyclic sort last forever. However, in the case where the sort is looking at two indices that have the same element, we just stop the
current iteration and move to the next element.

Once the sort is finished, the list will have all the correct elements in the right place except for the extra duplicated elements.
Those elements will be in the positions of the missing numbers. Now, we just go through the list and find where the index + 1 does
not match the element inside the index.

Time Complexity: O(N) - There are a maximum of O(N) iterations from the outer for loop. The inner while loop would give a maximum of 
                        N-1 swaps. The second outer for loop, iterates the list once as well. N + N + N -> O(N)
Space Complexity: O(1) - No extra space is needed.
'''


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(n).

Space complexity 
Ignoring the space required for the output array, the algorithm runs in constant space O(1).
'''
