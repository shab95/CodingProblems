def make_squares(arr):
    squares = []
    
    start, end = 0, len(arr) - 1
    
    while start <= end :
        if abs(arr[end]) > abs(arr[start]):
            squares.insert(0,arr[end] ** 2)
            end -= 1
        else:
            squares.insert(0,arr[start] ** 2)
            start += 1
    
    return squares

print(make_squares([-2,-1,0,2,3]))

print(make_squares([-3,-1,0,1,2]))