def fruitbasket(fruits):
    window_start = 0
    maxCount = 0
    fruitFrequency = {}
    for window_end in range(len(fruits)):
        fruit = fruits[window_end]
        if fruit not in fruitFrequency:
            fruitFrequency[fruit] = 0
        fruitFrequency[fruit] += 1
        while len(fruitFrequency) > 2:
            firstFruit = fruits[window_start]
            fruitFrequency[firstFruit] -= 1
            if fruitFrequency[firstFruit] == 0:
                del fruitFrequency[firstFruit]
            window_start += 1
        maxCount = max(maxCount, window_end - window_start + 1)

    return maxCount


'''
Summary:
The basis of the problem is to find the longest substring of 2 distinct characters in a string.

To solve the problem, we use the sliding window technique. We go through each of the fruits at the beginning of the list until we find
our third distinct fruit. While adding fruits, we keep count of how many of each fruit we have seen. At the third distinct fruit, we
remove the fruits we saw at the beginning until there are only 2 distinct fruits in our window again. In each iteration, we check
if the length of our window(number of fruits we have) is bigger than the previous max.

Time Complexity: O(N) - The outer for loop encounters each character exactly once. The inner while loop encounters each character exactly
                        once. N + N -> O(N)
                        
Space Complexity: O(1) - There's going to be a maximum of 3 fruits inside the hashmap. The extra fruit is in when we encounter the 3rd
                         distinct fruit.
'''


def main():

    print(str(fruitbasket(['A', 'B', 'C', 'A', 'C'])))
    print(str(fruitbasket(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
