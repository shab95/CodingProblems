def dutch_flag_sort(arr):
    zeroMarker = 0
    twoMarker = len(arr) - 1
    i = 0
    while i <= twoMarker:
        print(zeroMarker, i, twoMarker)
        print(arr)
        print()
        if arr[i] == 0:
            arr[i] = arr[zeroMarker]
            arr[zeroMarker] = 0
            zeroMarker += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i] = arr[twoMarker]
            arr[twoMarker] = 2
            twoMarker -= 1

    return arr


'''
Summary:
The goal of the problem is to sort an array full of 0s, 1s, and 2s. However, a better way of thinking about the problem is just by
finding the seperation of the 0s and 1s and the seperation for 1s and 2s. By finding the seperations, we would have already sorted
the problem. A great way to tackle this problem is by using the two pointers technique.

By using the two pointers technique, we set one pointer to the very beginning and one pointer to the very end. The pointer at the 
beginning will be where any 0s we come across swap into. The pointer at the end will be where any 2s we come across swap into. 
Let's call the pointer at the beginning our zero pointer and the one at the end our two pointer. When a zero is found, we will swap it 
into the place where zero pointer is at. We will continue to iterate and increase the zero pointer to the next index. When a one is 
found, we only continue to iterate. No swapping occurs. When a two is found, we will swap it into the place where two pointer is at.
We will then decrease the two pointer to the previous index. However, when we swap a two, we do not continue to iterate. Why?
When a two is swapped, we are swapping with a number that we have previously not seen before. It may be a one or a zero and if it is
a zero, then it must be swapped with the element at the zero pointer again. The reason we can iterate when we see zero is because
we know the zeroes accumulate at the beginning of the list. We know the zero pointer will be at the current point of iteration
or before. This means anything before i should be a 1 or a zero. 

To be concise, zero pointer always points to where we need the next zero to go if we see one and two pointer always points to where
we need the next two to go if we see one.

When do we stop the algorithm? We stop once we cross two pointer. Everything past two pointer is guaranteed to be a two, so nothing
needs to be swapped there.

Time Complexity: O(N) - We process each element a maximum of one time and iterating only once.
Space Complexity: O(1) - No extra space is needed.
'''


arr = [1, 0, 2, 1, 0]
print(dutch_flag_sort(arr))
print(arr)

arr = [2, 2, 0, 1, 2, 0]
print(dutch_flag_sort(arr))
print(arr)
