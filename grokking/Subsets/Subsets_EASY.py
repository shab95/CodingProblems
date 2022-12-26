def find_subsets(nums):
    subsets = []

    subsets.append([])
    for currentNumber in nums:
        print(currentNumber)
        n = len(subsets)
        for i in range(n):
            print("Inside range: ", i, end=' ')
            set = list(subsets[i])
            set.append(currentNumber)
            print("set: ", set)
            subsets.append(set)

        print(subsets, end='\n\n')
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  #  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
