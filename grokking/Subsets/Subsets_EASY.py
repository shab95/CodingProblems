def find_subsets(nums):
    subsets = []
    subsets.append([])
    for i in nums:
        subsetCount = len(subsets)
        for j in range(subsetCount):
            subset = list(subsets[j])
            subset.append(i)
            subsets.append(subset)
    return subsets


'''
Summary:

This problem can be solved by using a slightly modified BFS approach. We start off by adding an empty subset because this will be the 
basis for adding all other subsets. Now, the algorithm takes the first number and adds it to all the subsets we currently have. So now
our subsets will have the empty subset and a subset with only the first number. With the second number, we create subsets out of 
adding the second number to the empty subset and the subset with only the first number. This creates two additional subsets and our
total subsets length will be 4. We keep doing this for all numbers. Now, we can see that the empty subset serves the purpose of giving
individual numbers their own subset.

Time Complexity: O(2^N) - The amount of time it takes to add each element to all the subsets takes increasingly more time. By the time
                          we get to the last number there will have been 2^(N-1) subsets. As a result, we can say that it would tkae
                          N * 2^N time -> 2^N
Space Complexity: O(2^N) - The output array will take 2^N space.
'''


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  #  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
