def pair_with_targetsum(arr, target_sum):
    start, end = 0, len(arr) - 1
    while start < end:
        trialSum = arr[start] + arr[end]
        if trialSum < target_sum:
            start += 1
        elif trialSum > target_sum:
            end -= 1
        else:
            return [start, end]
    return [-1, -1]


'''
Summary:
This problem asks us to find two numbers that add up to a target sum. Because the list is sorted, we can use the two pointers trick to
our advantage. We put one pointer at the beginning of the array and one pointer at the end of the array, then take the sum. If the
sum is less than the target sum, that means we need a bigger number and move the start pointer up one index. This will increase the
sum because the list is sorted. If the sum is more than the target sum, that means we need a smaller number and move the end pointer
down one index. This will decrease the sum because the list is sorted. Eventually, we will find a combination that adds up to the 
target_sum. If the pair does not exist, then the end pointer will cross over the start pointer or the start pointer will cross over
the end pointer. 

Time Complexity: O(N) - We process each element a maximum of one time.
Space Complexity: O(1) - No extra space is used besides 3 variables.
'''


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
