## Problem from Book:
Congratulations! You’ve been hired by the giant online bookstore DeNile (“Not just a river in Egypt!”) to optimize their warehouse robots. Each book that DeNile sells has a unique ISBN (International Standard Book Number), which is just a numerical value. Each of DeNile’s warehouses contains a long row of bins, each containing multiple copies of a single book. These bins are arranged in sorted order by ISBN; each bin’s ISBN is printed on the front of the bin in machine-readable form. Books are retrieved from these bins by robots, which run along rails parallel to the row of bins. DeNile does not maintain a list of which bins contain which ISBN numbers; that would be too simple! Instead, to retrieve a desired book, the robot must first find that book’s bin using a binary search. Because the search requires physical motion by the robot, we can no longer assume that each step of the binary search requires O(1) time. 

## Specifics:
 * The robot always starts at the “0th bin” (where the books are loaded into boxes to ship to customers). 146 Exercises
 * Moving the robot from the ith bin to the jth bin requires α|i − j| seconds for some constant α.
 * The robot must be directly in front of a bin in order to read that bin’s ISBN. Reading an ISBN requires β seconds, for some constant β.
 * Reversing the robot’s direction of motion (from increasing to decreasing or vice versa) requires γ additional seconds, for some constant γ. 
* When the robot finds the target bin, it extracts one book from that bin and returns to “the 0th bin”. 

Design and analyze an algorithm to compute a binary search tree over the bins that minimizes the total time the robot spends searching for books. Your input is an array f [1 .. n] of integers, where f [i] is the number of times that the robot will be asked to retrieve a book from the ith bin, along with the time parameters α, β, and γ.


Before writing any code, create a brief write-up that clearly describes the answers to the following questions:

What is the original optimization problem?

what are the sub-problems and how many of them are total (i.e. what will be the number of items in the cache by the time you finish running the algorithm)? (hint: make sure that the sub-problem parameters are Hashable)

Which sub-problems can be immediately solved without needing recursion and what are the return values corresponding to those base-cases?

Give a recursive definition for how to solve an arbitrary parent sub-problem in terms of the children sub-problems. (Part of the effort is to identify the relevant children sub-problems for a given parent, and part of the effort is to describe how to combine the results of those children sub-problems to solve the parent problem).

Sub-problems will you use directly in solveing the original problem and how will you use their results?


## Adam's Advice in Teams:
Today we talked about optimal binary search trees when the only cost is a constant scan cost.

So, we said that to get the mincost to service the items that are in the range from start up to (but not including) end, we consider each possible root between start and end.  Regardless of the new root, each item that we search for will need to scan the root that we choose so that adds a cost that is equal to the total frequency in the range from start to end.  In addition, if we choose i to be the root of this span, we will need to add in the (recursively computed) best cost for the items from start up to i, and the best cost for items from i+1 up to end.   So, to pick, we just pick the option (the choice of i) that minimizes the total cost.
 
When considering the robot variation, though, in addition to adding in the cost to scan times the total frequency in the current span and the cost of the left tree and the right tree,  you will also need to apply the cost of moving from the previous root to the proposed i (again, multiplied by the total frequency since each probe will need to pay that), plus the cost of changing direction for the appropriate subset of the frequency (which depends on the proposed i).   
This will require that your subproblems include information about which direction the robot is starting when solving the sub problem (given that and the start and end indexes, you can compute where it used to be). Finally, you need to also account for the fact that the frequency at the new root will need to be delivered back to the start (which will include a potential change of direction and movement).
 
Anyway, I hope that helps.  As always, the goal is not just to solve this problem, but to understand the technique so that you can efficiently solve many custom problems like it that you might come up against. 


## Aaron Notes:
* The Robot knows Frequency.
* Changing Direction matters
* Hash the Boxes!!! (must be our own hash because we care about order to the end)
