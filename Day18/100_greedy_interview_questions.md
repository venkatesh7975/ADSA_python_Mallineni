# 100 Greedy Algorithms Interview Questions and Answers

## Section 1: Fundamentals of Greedy Algorithms (1-20)
1. **What is a Greedy Algorithm?**
   *Answer:* An algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit.
2. **What is the Greedy Choice Property?**
   *Answer:* A global optimum can be arrived at by selecting a local optimum.
3. **What is Optimal Substructure?**
   *Answer:* An optimal solution to the problem contains optimal solutions to the subproblems.
4. **Do greedy algorithms always yield optimal solutions?**
   *Answer:* No, they only yield optimal solutions for problems that possess the greedy choice property and optimal substructure.
5. **How does a greedy algorithm differ from dynamic programming?**
   *Answer:* Greedy makes the locally optimal choice without reconsidering it, while DP considers all overlapping subproblems and guarantees a global optimum.
6. **Can a problem be solved by both Greedy and DP?**
   *Answer:* Yes, many DP problems can be solved by Greedy if they exhibit the greedy choice property, usually with better performance.
7. **Name a classic problem where Greedy fails but DP succeeds.**
   *Answer:* 0/1 Knapsack Problem or Coin Change problem with arbitrary coin denominations.
8. **Why are greedy algorithms usually faster than DP?**
   *Answer:* Greedy algorithms do not evaluate all possible subproblems; they follow a single path to the solution.
9. **What is the typical time complexity of a Greedy Algorithm?**
   *Answer:* Often $O(N \log N)$ due to the initial sorting step, followed by $O(N)$ for the greedy choices.
10. **What data structure is commonly used to pick the next best choice in greedy algorithms?**
    *Answer:* Priority Queues (Min-Heap / Max-Heap) or sorted arrays.
11. **Is greedy a top-down or bottom-up approach?**
    *Answer:* Greedy algorithms are generally top-down, making a choice and then reducing the problem to a smaller subproblem.
12. **What does "locally optimal choice" mean?**
    *Answer:* The choice that looks the best at the current moment without considering future consequences.
13. **Give an example where the greedy approach gives the worst possible result.**
    *Answer:* Finding the longest path in a graph.
14. **How do you prove a greedy algorithm is correct?**
    *Answer:* Usually by mathematical induction, "greedy stays ahead" argument, or an exchange argument.
15. **What is an exchange argument?**
    *Answer:* A proof technique showing that any non-greedy optimal solution can be transformed into the greedy solution without worsening its cost.
16. **If a problem has optimal substructure but not the greedy choice property, which paradigm is best?**
    *Answer:* Dynamic Programming.
17. **What happens if multiple choices are equally "greedy"?**
    *Answer:* The algorithm can pick any of the ties; in some problems, tie-breaking rules are needed.
18. **Is Greedy approach memory efficient?**
    *Answer:* Yes, it usually requires $O(1)$ auxiliary space beyond storing the input, unlike DP which often needs matrices.
19. **What is a "matroid"?**
    *Answer:* A mathematical structure that generalizes the notion of linear independence; greedy algorithms find optimal solutions on matroids.
20. **Can graphs be processed using greedy algorithms?**
    *Answer:* Yes, algorithms like Dijkstra's, Prim's, and Kruskal's are based on the greedy approach.

## Section 2: Standard Greedy Algorithms (21-40)
21. **What is Huffman Coding?**
    *Answer:* A greedy algorithm used for lossless data compression by assigning variable-length codes based on character frequencies.
22. **What property makes Huffman Coding optimal?**
    *Answer:* Prefix-free property, meaning no code is a prefix of another, preventing ambiguity.
23. **What data structure is used to build a Huffman Tree?**
    *Answer:* A Min-Priority Queue.
24. **What is the time complexity of building a Huffman Tree?**
    *Answer:* $O(N \log N)$ where N is the number of unique characters.
25. **What does Kruskal’s Algorithm do?**
    *Answer:* Finds the Minimum Spanning Tree (MST) of a graph by sorting edges and greedily picking the smallest edge that doesn't form a cycle.
26. **What data structure does Kruskal’s use to detect cycles?**
    *Answer:* Disjoint Set (Union-Find).
27. **What is the time complexity of Kruskal’s Algorithm?**
    *Answer:* $O(E \log E)$ or $O(E \log V)$ due to sorting edges.
28. **What does Prim’s Algorithm do?**
    *Answer:* Finds the MST by starting with a single node and greedily adding the smallest edge connecting the growing tree to a new vertex.
29. **When is Prim’s preferred over Kruskal’s?**
    *Answer:* Prim’s is better for dense graphs, while Kruskal’s is better for sparse graphs.
30. **What is Dijkstra’s Algorithm?**
    *Answer:* A greedy algorithm to find the shortest path from a single source to all other vertices in a graph with non-negative edge weights.
31. **Why does Dijkstra’s algorithm fail with negative weights?**
    *Answer:* It assumes that once a node is processed, its shortest path is permanently found, which a negative edge might violate.
32. **What data structure makes Dijkstra’s algorithm efficient?**
    *Answer:* A Min-Priority Queue.
33. **Is the Bellman-Ford algorithm greedy?**
    *Answer:* No, it uses Dynamic Programming principles to handle negative weights.
34. **Does finding the maximum spanning tree use a greedy approach?**
    *Answer:* Yes, by modifying Kruskal's or Prim's to pick the maximum weight edge at each step.
35. **What is the Egyptian Fraction problem?**
    *Answer:* Expressing a given fraction as a sum of unique unit fractions. It can be solved greedily by always picking the largest possible unit fraction.
36. **Is Graph Coloring solved optimally with a greedy algorithm?**
    *Answer:* No, greedy graph coloring provides a valid coloring but not necessarily the minimum chromatic number.
37. **What is the greedy strategy for Graph Coloring?**
    *Answer:* Assign the smallest available color to a vertex that hasn't been used by its neighbors.
38. **How does greedy handle the Set Cover problem?**
    *Answer:* By repeatedly picking the set that covers the maximum number of remaining uncovered elements (gives an approximation, not optimal).
39. **Is the greedy solution to Set Cover optimal?**
    *Answer:* No, it is a $O(\log N)$ approximation algorithm.
40. **Can you find the Longest Common Subsequence using a greedy approach?**
    *Answer:* No, DP is required because greedy choices can lead to a dead-end.

## Section 3: Scheduling and Activity Selection (41-60)
41. **What is the Activity Selection Problem?**
    *Answer:* Finding the maximum number of non-overlapping activities that can be performed by a single person.
42. **What is the optimal greedy choice for Activity Selection?**
    *Answer:* Sort activities by finish time and always pick the activity that finishes earliest and doesn't overlap with previously picked ones.
43. **Why sort by finish time instead of start time in Activity Selection?**
    *Answer:* Picking the earliest finish time leaves the maximum possible free time for remaining activities. Sorting by start time doesn't guarantee this.
44. **What is the Job Sequencing Problem with Deadlines?**
    *Answer:* Maximizing total profit by scheduling jobs where each job takes 1 unit of time and has a deadline and profit.
45. **What is the greedy strategy for Job Sequencing?**
    *Answer:* Sort jobs in descending order of profit and assign each job to the latest possible free slot before its deadline.
46. **How can Job Sequencing be optimized from $O(N^2)$ to $O(N \log N)$?**
    *Answer:* By using Disjoint Sets (Union-Find) to keep track of available time slots.
47. **What is Shortest Job First (SJF) scheduling?**
    *Answer:* A greedy CPU scheduling algorithm that selects the waiting process with the smallest execution time.
48. **What does SJF try to minimize?**
    *Answer:* Average waiting time.
49. **What is the preemptive version of SJF?**
    *Answer:* Shortest Remaining Time First (SRTF).
50. **How does SRTF differ from SJF?**
    *Answer:* In SRTF, if a newly arrived process has a shorter burst time than what is remaining for the current process, the CPU is preempted.
51. **Can SJF cause starvation?**
    *Answer:* Yes, long jobs may never execute if short jobs keep arriving.
52. **What is the Minimum Number of Platforms problem?**
    *Answer:* Finding the minimum railway platforms needed given train arrival and departure times so no train waits.
53. **How is the Platforms problem solved greedily?**
    *Answer:* Sort all arrivals and departures. Iterate through time, incrementing platforms on arrival and decrementing on departure, tracking the maximum.
54. **What is the Interval Partitioning Problem?**
    *Answer:* Finding the minimum number of resources to schedule all intervals without overlaps.
55. **What is the greedy strategy for Interval Partitioning?**
    *Answer:* Sort intervals by start time. Assign each to an available resource, or allocate a new one if none are free.
56. **What data structure is useful for Interval Partitioning?**
    *Answer:* A Min-Heap to track the earliest finish time among currently allocated resources.
57. **Can round-robin scheduling be considered greedy?**
    *Answer:* No, it distributes time equally rather than making locally optimal choices based on attributes like burst time.
58. **Why does sorting by duration fail for the Activity Selection problem?**
    *Answer:* A short activity might sit right in the middle of a large time slot, preventing two other activities from being scheduled.
59. **In scheduling to minimize maximum lateness, what is the greedy choice?**
    *Answer:* Earliest Deadline First (EDF).
60. **Does Earliest Deadline First (EDF) guarantee minimizing max lateness?**
    *Answer:* Yes, it is proven optimal via an exchange argument.

## Section 4: Knapsack and Coin Change (61-80)
61. **What is the Fractional Knapsack Problem?**
    *Answer:* Selecting items with given weights and values to maximize total value in a capacity-constrained knapsack, allowing fractions of items.
62. **What is the greedy strategy for Fractional Knapsack?**
    *Answer:* Sort items by value-to-weight ratio in descending order and greedily add the highest ratio items.
63. **What is the time complexity of Fractional Knapsack?**
    *Answer:* $O(N \log N)$ to sort, and $O(N)$ to iterate. Total $O(N \log N)$.
64. **Why doesn't the greedy approach work for 0/1 Knapsack?**
    *Answer:* In 0/1 Knapsack, you cannot take fractions. The greedy choice might leave empty space that could have been better utilized by other combinations.
65. **What paradigm is used for 0/1 Knapsack?**
    *Answer:* Dynamic Programming.
66. **What is the Coin Change Problem?**
    *Answer:* Finding the minimum number of coins needed to make a certain amount of change.
67. **When does the greedy algorithm work for Coin Change?**
    *Answer:* When the coin denominations form a "canonical" coin system (e.g., US currency: 1, 5, 10, 25).
68. **When does the greedy algorithm fail for Coin Change?**
    *Answer:* When denominations are arbitrary (e.g., coins of 1, 3, 4, and amount is 6. Greedy gives 4+1+1=3 coins, DP gives 3+3=2 coins).
69. **How do you solve the Coin Change problem for arbitrary denominations?**
    *Answer:* Using Dynamic Programming.
70. **What is the greedy choice in the Coin Change problem?**
    *Answer:* Always pick the largest coin denomination that is less than or equal to the remaining amount.
71. **What is the "Water Connection Problem"?**
    *Answer:* Finding the optimal way to lay pipes between houses given a set of existing connections, often solved by greedy graph traversal.
72. **What is the Police and Thieves problem?**
    *Answer:* Given an array of police and thieves, finding the maximum thieves that can be caught if a policeman can catch a thief within $K$ distance.
73. **What is the greedy strategy for Police and Thieves?**
    *Answer:* Use two pointers, one for police and one for thieves, matching the earliest available policeman with the earliest available thief within range $K$.
74. **In the Minimum Cost to Connect Ropes problem, what is the greedy choice?**
    *Answer:* Always connect the two shortest ropes available.
75. **What data structure is ideal for the Connect Ropes problem?**
    *Answer:* A Min-Priority Queue.
76. **How does the fractional knapsack handle items of equal value/weight ratio?**
    *Answer:* Any order works; it will not affect the maximum total value.
77. **Can greedy algorithm handle Fractional Knapsack with multiple knapsacks?**
    *Answer:* No, Multiple Knapsack problems are typically NP-Hard.
78. **What is the classic "Jump Game" on LeetCode?**
    *Answer:* Given an array of maximum jump lengths, determine if you can reach the last index.
79. **How do you solve Jump Game greedily?**
    *Answer:* Keep track of the maximum reachable index. If the current index is greater than the max reachable, you can't reach the end.
80. **How do you find the minimum number of jumps to reach the end (Jump Game II)?**
    *Answer:* Keep track of the current jump boundary and the farthest you can reach. When you hit the boundary, increment jump count and update the boundary.

## Section 5: Edge Cases, Advanced Applications & Misc (81-100)
81. **What is the Candy distribution problem (LeetCode 135)?**
    *Answer:* Distributing candies to children in a line based on ratings such that higher-rated children get more than their neighbors.
82. **How is the Candy problem solved greedily?**
    *Answer:* Two passes: left-to-right (ensuring right child > left child) and right-to-left (ensuring left child > right child).
83. **Can you solve the Maximum Subarray Sum (Kadane's Algorithm) using greedy logic?**
    *Answer:* Yes, Kadane's greedily adds to the current sum but resets it to 0 if it becomes negative.
84. **What is the "Assign Cookies" problem?**
    *Answer:* Given children's greed factors and cookie sizes, maximize content children. Solved greedily by matching the smallest cookie to the smallest acceptable greed factor.
85. **What is the Gas Station (Circular Tour) problem?**
    *Answer:* Finding a starting gas station to complete a circular route without running out of gas.
86. **How is the Gas Station problem solved greedily?**
    *Answer:* If total gas < total cost, return -1. Otherwise, traverse the array tracking current gas; if it drops below 0, reset start point to the next station.
87. **What is the Minimum spanning tree of a directed graph called?**
    *Answer:* An Arborescence (found using Chu-Liu/Edmonds' algorithm, which incorporates greedy concepts but is more complex).
88. **What is a Greedy Heuristic?**
    *Answer:* An approach used in NP-Hard problems (like Traveling Salesperson) to find a "good enough" approximation quickly.
89. **Describe the Nearest Neighbor heuristic for the TSP.**
    *Answer:* Start at a random city and repeatedly visit the nearest unvisited city. It's a greedy approach that does not guarantee an optimal tour.
90. **Why does Prim's algorithm guarantee an MST?**
    *Answer:* Because of the "cut property"; the lightest edge crossing any cut of a graph must belong to the MST.
91. **What is the "Task Scheduler" problem (LeetCode 621)?**
    *Answer:* Scheduling CPU tasks with cooling periods to minimize overall time.
92. **What is the greedy strategy for Task Scheduler?**
    *Answer:* Schedule the most frequent tasks first, inserting them into available cooling slots.
93. **What is the 'Meeting Rooms II' problem?**
    *Answer:* Finding the minimum number of conference rooms required for a given set of meeting intervals (same as Interval Partitioning).
94. **How do you reconstruct an original string given its characters' frequency and avoiding identical adjacent characters?**
    *Answer:* Greedily pick the most frequent character that is different from the previous one (using a Max-Heap).
95. **Does the greedy method help in graph traversal (BFS/DFS)?**
    *Answer:* BFS and DFS are uninformed searches, but Best-First Search and A* use greedy heuristics to guide the traversal.
96. **In finding the Minimum Spanning Forest of a disconnected graph, does Kruskal's still work?**
    *Answer:* Yes, it simply terminates when all possible safe edges are added, yielding an MSF.
97. **Can we find the Shortest Path in a Directed Acyclic Graph (DAG) greedily?**
    *Answer:* Yes, by doing a topological sort and greedily relaxing edges, which runs in linear time $O(V+E)$.
98. **Are Greedy Algorithms always deterministic?**
    *Answer:* Yes, standard greedy algorithms are deterministic, though ties can be broken arbitrarily.
99. **How do you decide between Greedy and DP in an interview?**
    *Answer:* Try to find a counter-example where the greedy choice fails. If you find one, use DP. If not, try to prove the greedy choice mathematically.
100. **Summarize the main advantage of Greedy Algorithms.**
     *Answer:* They are typically easy to conceptualize and simple to implement, running much faster than exhaustive search or DP when applicable.
