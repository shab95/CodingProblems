def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        target = 0 - arr[i]
        left = i + 1
        right = len(arr) - 1

        while (left < right):
            if arr[left] + arr[right] == target:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left > 0 and arr[left] == arr[left - 1]:
                    left += 1
                while right < len(arr) - 1 and arr[right] == arr[right + 1]:
                    right -= 1
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1

    return triplets


'''
Summary:

This algorithm has many parts to it, but the two pointers technique is the main solution to the problem. First, the array must be sorted.
This helps both avoiding duplicates and finding triplets. After sorting, we iterate through the list. If the element we are currently
looking it as is the same as the one that came before it, then we can skip it. This will help avoid duplicate triplets.

Once we encounter a unique number, the goal is to find two numbers that add up to the negation of the unique number. Because
we are looking for a unique triplet, we know we don't have to comb through the elements that came before it in the array. As a result,
we set a left pointer to the index of the element we have iterated to in the for loop plus one. If the for loop is at index 2, 
we set left to 3. We always set the right pointer to the end of the array. Now, we run the pair target algorithm with two pointers
that we have used before. However, we have to be careful of duplicates again. We can do this by checking each time triplet has been found. 
Once a triplet has been found, any duplicate of the left pointer element is skipped and duplicate of the right pointer element is skipped.

Time Complexity: O(N^2) - The for loop on the outside runs across every element which is an O(N) operation. The while loop on the inside
                          is an O(N) operation happening on every for loop iteration. Sorting does take NlogN, but asymptotically, N^2 
                          is bigger. N * N  + NlogN - > N^2
Space Complexity: O(N) -  Python uses Tim sort, so space is used to sort. No extra space is used in the algorithm besides the output 
                          array.

'''
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))
print(search_triplets([-1, -1, 2]))
