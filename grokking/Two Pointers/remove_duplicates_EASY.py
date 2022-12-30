'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''


# answer
def remove_duplicates(arr):
    nextNonDuplicate = 1
    for next in range(1, len(arr)):
        if arr[nextNonDuplicate - 1] != arr[next]:
            arr[nextNonDuplicate] = arr[next]
            nextNonDuplicate += 1
            next += 1
        else:
            next += 1
    print(arr[:nextNonDuplicate])
    return nextNonDuplicate


'''
Summary:

This problem uses the two pointer technique. Because the array is sorted, we know exactly where each non duplicate element should end up
and all duplicate elements are right next to each other. That means when we encounter a duplicate element we can iterate right past it
until we find an element that is not a duplicate element.

With these facts, we can create an algorithm that avoids all duplicates. We have two pointers. One to iterate through the list and
past duplicates to find elements that have not been seen yet. Also, one pointer to keep track of where the next non duplicate element
should be placed. The next non duplicate pointer will initially point to index 1, since we know index 0 is not a duplicate itself.
The next pointer also starts at index 1. Let's say for example that index 1 is a duplicate of index 0. Then the next pointer will
iterate through index 2...n-1 until it finds a non duplicate of index 0. Once it finds a non duplicate, then we can copy the element
in that index to the non duplicate pointer's index(which is 1 right now). Once the copy happens, both pointers are increased by one. 
Now, the next pointer will continue until it finds a number that is not a duplicate of the number that was just copied to the previous
value of the nonDuplicate pointer.
'''


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
