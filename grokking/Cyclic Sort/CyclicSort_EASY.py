def cyclic_sort(nums):
    count = 0
    while count < len(nums):
        j = nums[count]-1
        if nums[count] != count + 1:
            nums[count], nums[j] = nums[j], nums[count]
        else:
            count += 1

    return nums


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

print(cyclic_sort([3, 1, 5, 4, 2]))
