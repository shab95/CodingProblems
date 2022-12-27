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


# answer
def find_missing_numbers(nums):
    for i in range(len(nums)):
        ithElement = nums[i]
        while (ithElement < len(nums) and i != nums[ithElement]):
            # swap
            nums[i] = nums[ithElement]
            nums[ithElement] = ithElement
            ithElement = nums[i]

    for i in range(len(nums)):
        if i != nums[i]:
            return i

    return len(nums)


'''
Summary:
Basis of the problem is that you have an array with n distinct elements. Each element is between 0 and n. This means there are n+1
elements in the array. 

The first issue is determining the correct spot for each element. If the first element is missing(0 is missing), then that means
the correct spot for the number "1" would be in the zeroeth index. However, if the last element is missing, then that means
the correct spot for the number "1" would be in the first index.

Now, in this coding scenario we addressed the correct spot for each index as the value of the index itself(0 goes in index 0, 1
goes in index 1,etc.). But you could do just the opposite too(1 goes in index 0, n goes in indeex n - 1).

Now, the next issue is where we place the last number(n) if we come accross it. The solution to this problem is actually ignoring it.
When iterating through the list and swapping numbers less than n to the right place, eventually n will be sitting in the spot where
the missing number is. After all the swaps take place. We iterate through the list one more time. If we find an index where
the element in the index doesn't match the index(n should be there), then that's our missing number. However, if all the indexes
do match with all the elements, then that means n is our missing number.

Time Complexity: O(N) - Iterating through each element once(O(N)). Maximum swaps is N-1(O(N)). One more iteration to check missing #(O(N)).

Space Complexity: O(1) - No extra space used.

'''


def main():
    print(find_missing_numbers([4, 0, 3, 1]))
    print(find_missing_numbers([8, 3, 5, 2, 4, 6, 0, 1]))


main()
