def make_squares(arr):
    squares = []
    left, right = 0, 0

    while (arr[right] < 0):
        right += 1

    left = right - 1
    print(left, right)
    while (left > -1 or right < len(arr)):
        if left <= -1:
            squares.append(arr[right] ** 2)
            right += 1
        elif right >= len(arr):
            squares.append(arr[left]**2)
            left -= 1
        else:
            if abs(arr[left]) > abs(arr[right]):
                squares.append(arr[right] ** 2)
                right += 1
            else:
                squares.append(arr[left] ** 2)
                left -= 1
    return squares


'''
Summary:

The problem requires the two pointers technique. There's two ways to go about this algorithm. The above algorithm requires you to find
the point where 0 is in the array. We place the one pointer here and one pointer at the index before. We find which pointer has an
element with a lower absolute value and add the square of that element to the squares array. We do this until both pointer run go past
the array's boundaries.

Time Complexity: O(N) - It can take a maximum of N to find 0. The second while loop processes each number once, so that's another N.
                        N + N -> O(N)
Space Complexity: O(N) - The output array is the same size as the input array.

Scroll down for a slightly more optimal technique.
'''

# ***** SECOND SOLUTION *****


def make_squares(arr):
    left, right = 0, len(arr) - 1
    squares = [0 for x in range(len(arr))]
    currentSquaresIndex = len(arr) - 1

    while (currentSquaresIndex > -1):
        if abs(arr[left]) < abs(arr[right]):
            squares[currentSquaresIndex] = arr[right] ** 2
            right -= 1
        else:
            squares[currentSquaresIndex] = arr[left] ** 2
            left += 1
        currentSquaresIndex -= 1

    return squares


'''
Summary:

This technique is more optimal because we do not try to find 0. Basically, we put a pointer at each end of the array. Whichever
pointer has an element with the higher absolute value gets squared and put in the last possible index of a list we initialized
to 0 before. Once the pointers cross, we know all elements have been covered. It is theoretically, slightly faster since we know we 
don't have to go find the index where 0 is.

Time Complexity: O(N) - Process each element once with the while loop.
Space Complexity: O(N) - Output array is the same size as the input array.
'''

print(make_squares([-2, -1, 0, 2, 3]))

print(make_squares([-3, -1, 0, 1, 2]))
