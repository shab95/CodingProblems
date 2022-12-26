def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAscending = arr[0] < arr[1]
    while start <= end:
        midInd = start + (end-start)//2
        mid = arr[midInd]
        if mid == key:
            return midInd

        if isAscending:
            if mid < key:
                start = midInd + 1
            else:
                end = midInd - 1
        else:
            if mid < key:
                end = midInd - 1
            else:
                start = midInd + 1
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
