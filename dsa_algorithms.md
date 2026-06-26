# DSA Algorithms - Interview Questions

This document covers common algorithmic paradigms including Sorting, Searching, Dynamic Programming, Greedy Algorithms, and Graph Traversals.

## 1. Searching and Sorting

**Q1. What is Binary Search? What is its time complexity?**
**A:** Binary search is an efficient algorithm for finding an item from a **sorted** list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed the possible locations to just one.
- **Time Complexity:** $O(\log n)$
- **Prerequisite:** The array MUST be sorted.

**Q2. Explain Merge Sort and its time complexity.**
**A:** Merge Sort is a **Divide and Conquer** algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
- **Time Complexity:** $O(n \log n)$ in the worst, average, and best cases.
- **Space Complexity:** $O(n)$ because it requires an auxiliary array for the merging process.

**Q3. Explain Quick Sort. Why is it often preferred over Merge Sort despite the same average time complexity?**
**A:** Quick Sort is also a Divide and Conquer algorithm. It picks an element as a "pivot" and partitions the given array around the picked pivot (putting smaller elements to the left, larger to the right).
- **Time Complexity:** Average case $O(n \log n)$, Worst case $O(n^2)$ (if the pivot is always the smallest or largest element).
- **Preference:** It is often preferred for arrays because it is an **in-place** sorting algorithm (requires only $O(\log n)$ auxiliary space for the recursion stack) and exhibits good cache locality, making it practically faster in many memory architectures.

## 2. Dynamic Programming (DP)

**Q4. What is Dynamic Programming? What two properties must a problem have to be solved using DP?**
**A:** Dynamic Programming is an optimization over plain recursion. Whenever we see a recursive solution that has repeated calls for same inputs, we can optimize it using DP by storing the results of subproblems.
The two properties are:
1. **Overlapping Subproblems:** The problem can be broken down into subproblems which are reused multiple times.
2. **Optimal Substructure:** The optimal solution to the given problem can be obtained from the optimal solutions of its subproblems.

**Q5. What is the difference between Memoization and Tabulation in DP?**
**A:**
- **Memoization (Top-Down):** Start solving the given problem by breaking it down. If you see that the subproblem has been solved already, just return the saved answer. If it hasn't been solved, solve it and save the answer (usually in a dictionary or array).
- **Tabulation (Bottom-Up):** Start solving the lowest level subproblems and build up to the main problem. It is usually implemented using iteration (loops) and an array/table to store values. It avoids recursion overhead.

**Q6. Give an example of a common DP problem.**
**A:** The **Fibonacci sequence**. A naive recursive approach takes $O(2^n)$ time due to recalculating the same values. Using DP (storing previously computed values), the time complexity drops to $O(n)$.
Other famous DP problems: 0/1 Knapsack, Longest Common Subsequence (LCS), Edit Distance, Coin Change.

## 3. Greedy Algorithms

**Q7. What is a Greedy Algorithm? How does it differ from DP?**
**A:** A greedy algorithm builds up a solution piece by piece, always choosing the next piece that offers the most immediate (local) benefit, with the hope that this local optimum will lead to a global optimum.
- **Difference from DP:** DP explores all possible choices to find the optimal one, which guarantees correctness but takes more time. A greedy approach makes the best choice at the moment and never reconsiders it. Greedy is faster but doesn't guarantee an optimal solution for every type of problem (it only works if the problem has the "Greedy Choice Property").

**Q8. Name some algorithms that use the Greedy approach.**
**A:** 
- Dijkstra's Shortest Path Algorithm
- Kruskal's Minimum Spanning Tree
- Prim's Minimum Spanning Tree
- Huffman Coding
- Activity Selection Problem

## 4. Graph Traversals and Algorithms

**Q9. Explain Breadth-First Search (BFS).**
**A:** BFS is a traversal algorithm for graphs and trees. It starts at the tree root (or some arbitrary node of a graph) and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- **Data Structure used:** Queue.
- **Use cases:** Finding the shortest path in an unweighted graph, web crawlers, level-order tree traversal.

**Q10. Explain Depth-First Search (DFS).**
**A:** DFS is a traversal algorithm that goes as deep as possible along each branch before backtracking.
- **Data Structure used:** Stack (often implicit via the call stack in recursion).
- **Use cases:** Topological sorting, detecting cycles in a graph, pathfinding in mazes.

**Q11. How do you find the Shortest Path in an unweighted graph vs a weighted graph?**
**A:**
- **Unweighted Graph:** Use BFS. Since all edges have the same weight, the first time you reach a node via BFS guarantees you've taken the fewest number of edges.
- **Weighted Graph (positive weights):** Use Dijkstra's Algorithm (a greedy approach using a Min-Heap priority queue).
- **Weighted Graph (with negative weights):** Use the Bellman-Ford algorithm (can also detect negative weight cycles).

## 5. Backtracking

**Q12. What is Backtracking?**
**A:** Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time ("backtracking" to previous valid states).

**Q13. What is a famous Backtracking problem?**
**A:** 
- **The N-Queens Problem:** Placing N chess queens on an $N \times N$ chessboard so that no two queens threaten each other.
- **Sudoku Solver:** Trying digits 1-9 in empty spaces, moving forward if valid, and backtracking if a contradiction is found.
- **Generating Permutations/Subsets.**
