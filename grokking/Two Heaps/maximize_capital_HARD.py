'''
Problem Statement 
Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit.

We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

Example 1:

Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
Output: 6
Explanation:

With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:

Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0, Number of Projects=3
Output: 8
Explanation:

With ‘0’ capital, we can only select the first project, bringing out capital to 1.
Next, we will select the second project, which will bring our capital to 3.
Next, we will select the fourth project, giving us a profit of 5.
After selecting the three projects, our total capital will be 8 (1+2+5).
'''


# mycode
from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    # TODO: Write your code here
    minCapitalHeap = []
    maxProfitHeap = []

    # adding capitals in min heap to determine which projects are the cheapest
    for i in range(len(capital)):
        heappush(minCapitalHeap, (capital[i], i))

    for i in range(numberOfProjects):

        while len(minCapitalHeap) > 0 and minCapitalHeap[0][0] <= initialCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, -1 * profits[i])

        if len(maxProfitHeap) < 1:
            return initialCapital

        initialCapital += -1 * heappop(maxProfitHeap)

    return initialCapital


'''
Summary:

This problem can be solved by using two heaps. 

The first heap is a min heap that stores the capitals of all the projects. The second heap is a max heap that stores the profits of
all the projects you can afford with your capital. The min heap is made before we pick the projects that we want to do. Once we enter
the for loop to pick projects that's where we add the projects we can afford to a max heap. We do this by popping projects off the top 
of the min heap that we can afford. This is why we have the minCapitalHeap[0][0] <= initialCapital. We push the profit of these projects
that we know we can afford onto the max profit heap. This allows us to get the most profitable project that we can afford. However,
there is a possibility that there are no projects we can afford. This is when we simply return our final number. However, if there
is a project we can afford and we are in the for loop, then we can add the most profitable project to our initialCapital. This
most profitable project will be the top of the max profit heap.

Time Complexity: O(NlogN + KlogN) - At max we push all the projects to both heaps. This is where we get NlogN. Since we are selecting K
                                    projects from the top of the max heap, that is another klogN.
Space Complexity: O(N) - We store all the projects in heaps.
'''


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
