'''
Problem Statement 
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

# mycode


def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    startingPoint, endingPoint = 0, 0
    for i in range(len(nums)):
        startingPoint = 0
        if i > 0 and nums[i] == nums[i - 1]:
            startingPoint = endingPoint + 1
        endingPoint = len(subsets) - 1

        for j in range(startingPoint, endingPoint + 1):
            subset = list(subsets[j])
            subset.append(nums[i])
            subsets.append(subset)
    return subsets


'''
Summary:

This problem can be solved very similarly to the normal subsets problem. The only difference here is we have to understand where 
duplicate subsets form. 
First, we will sort the nums list so we can get duplicates right next to each other and it will be easier to detect duplicates. Next,
we have to understand how duplicate subsets can form. Pretend our nums is [1,3,3]. The first 3 will create subsets [3] and [1,3]. If
we did what we did before with the second 3, our duplicate would become [3] and [1,3] as well. However, we don't want the duplicates
we only want the new subsets that the second 3 would bring and that would be [3,3] and [1,3,3]. As a result, we can see that adding
the second 3 to anything that existed before the first 3 was processed would create duplicates(meaning we shouldnt add the second 3 to
[] and [1] again). Instead we should only create the subsets off of what was formed when the first 3 was processed(means only add it to
[3] and [1,3]). This way we avoid duplicates. 

We can keep track of where to add the current number by using starting and ending points. If the current number is not a duplicate, then
our startingPoint would be zero and our endingPoint would be the  end of the list. If our current number is a duplicate, then our 
startingPoint would be the ending of the previous element in the list(the non duplicate). This way the only subsets we are adding the
duplicate to would be the brand new ones introduced by the first copy of the duplicate(first encounter).

Time Complexity: O(2^N) - Each time we add numbers to the previous subsets, the amount of subsets increase. At max we will have to add
                          the current number to 2^(N-1) subsets.
Space Complexity: O(2^N) - At most our output array will contain 2^N subsets.
'''


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
