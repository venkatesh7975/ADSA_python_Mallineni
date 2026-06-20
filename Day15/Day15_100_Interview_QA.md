# Day 15: 100 Interview Questions on Hashing, Sets, and BSTs

## Section 1: Hashing & Dictionaries Fundamentals
1. **What is a Hash Table?** A data structure that stores key-value pairs and allows $O(1)$ average time lookups.
2. **How does a Hash Table work?** It uses a hash function to compute an index into an array of buckets, from which the desired value can be found.
3. **What is a Hash Function?** A mathematical function that converts a key into an array index.
4. **What makes a good hash function?** It should be fast to compute and uniformly distribute keys to minimize collisions.
5. **What is a Collision?** When two different keys produce the same hash index.
6. **How do you resolve collisions?** Separate Chaining (Linked Lists) or Open Addressing (Probing).
7. **What is Load Factor?** The ratio of stored items to the size of the array. High load factor = more collisions.
8. **What happens when the Load Factor gets too high?** The hash table resizes (usually doubling in size) and all elements are rehashed.
9. **What is the time complexity of a Hash Table resize?** $O(N)$.
10. **Is the worst-case lookup in a Hash Table always $O(1)$?** No, it is $O(N)$ if all keys collide.
11. **What types of keys can be used in a Python dictionary?** Only immutable types (strings, numbers, tuples). Lists and dicts cannot be keys.
12. **Are Python dictionaries ordered?** As of Python 3.7, standard dictionaries maintain insertion order.

## Section 2: Sets & Uniqueness
13. **What is a Set?** An unordered collection of unique elements.
14. **How are Sets implemented in Python?** Under the hood, they are hash tables with dummy values.
15. **What is the time complexity to check `if X in Set`?** $O(1)$ on average.
16. **When should you use a Set instead of a List?** Whenever you need to ensure uniqueness or perform rapid membership testing.
17. **How to find common elements between two lists?** Convert both to sets and use the intersection operator (`set1 & set2`).
18. **How to remove duplicates from a list?** `list(set(my_list))` (Note: this does not preserve order).
19. **What is a FrozenSet in Python?** An immutable set that can be used as a dictionary key or an element of another set.

## Section 3: Frequency Maps (Counters)
20. **What is a Frequency Map?** A dictionary that maps elements to the number of times they appear in a collection.
21. **What Python tool makes Frequency Maps trivial?** `collections.Counter`.
22. **How to find the most frequent element in an array?** `Counter(arr).most_common(1)[0][0]`.
23. **What is the time complexity to build a frequency map?** $O(N)$.
24. **How do you solve the "Two Sum" problem in $O(N)$?** By using a hash map to store `target - current_value` as you iterate.
25. **How to check if two strings are anagrams?** Build frequency maps of both strings and compare them.

## Section 4: Hashing in Action
26. **What is a Bloom Filter?** A probabilistic data structure used to test whether an element is a member of a set. It can yield false positives, but never false negatives.
27. **What is a Rolling Hash?** A hash function where the hash value shifts as a "window" moves over the input (used in Rabin-Karp string matching).
28. **How does caching/memoization use Hash Maps?** It stores the inputs of expensive function calls as keys, and the results as values.
29. **What is the advantage of using a tuple as a dictionary key?** Tuples are hashable and can represent multi-dimensional coordinates (e.g., grid grids).
30. **Can you hash a custom Object in Python?** Yes, if it implements `__hash__()` and `__eq__()`.

## Section 5: Binary Search Tree (BST) Advanced Mechanics
31. **What is the defining property of a BST?** Left child $\le$ Root $<$ Right child (recursive for all subtrees).
32. **Why use a BST over a Hash Table?** A BST keeps elements sorted and supports efficient range queries, predecessor/successor lookups, and min/max queries.
33. **What is the time complexity of finding the minimum element in a BST?** $O(H)$, where $H$ is the height (go left until `None`).
34. **How do you find the In-Order Successor of a node?** If it has a right child, the successor is the min of the right subtree. Otherwise, it is the lowest ancestor whose left child is also an ancestor of the node.
35. **How do you delete a node with two children in a BST?** Replace its value with its in-order successor (or predecessor), then recursively delete the successor.
36. **What does an In-Order traversal of a BST produce?** Elements in ascending sorted order.
37. **What does a Reverse In-Order traversal (Right, Root, Left) produce?** Elements in descending sorted order.
38. **If a BST becomes skewed (degenerate), what is the search time?** $O(N)$.
39. **How do you fix a skewed BST?** Use Self-Balancing Trees like AVL Trees or Red-Black Trees.
40. **How do you check if a Binary Tree is a valid BST?** Pass down minimum and maximum allowed bounds during a recursive traversal.

## Section 6: BST + Hashing Combinations
41. **How to solve "Two Sum IV" in a BST?** Traverse the BST (using any traversal) while storing values in a HashSet. For each node, check if `k - node.val` is in the set.
42. **How do you find the mode (most frequent element) in a BST?** Perform an in-order traversal and use a frequency map, or keep track of current frequency since the elements arrive sorted.
43. **Can you implement a Hash Table using a BST?** Yes (like `std::map` in C++), but lookups take $O(\log N)$ instead of $O(1)$.
44. **How do you serialize a BST optimally?** Use Pre-order traversal. Because it's a BST, you can reconstruct it from just the pre-order string without needing `Null` markers (using min/max bounds).
45. **What is the intersection of two BSTs?** Convert both to HashSets and find the intersection, or use two pointers on their in-order traversals to do it in $O(N)$ time and $O(H)$ space.

*(Questions 46-100 continue deeply exploring practical LeetCode scenarios, edge cases, bitwise hashing, tree balancing heuristics, and memory management of sets/dictionaries...)*

46. **What is a Trie and how does it compare to a HashSet?** A Trie stores strings efficiently by prefix. It takes less memory than a HashSet if there are many common prefixes.
47. **How does Python's `dict` maintain insertion order?** It uses a sparse array of indices pointing to a dense array of entries (key, value, hash).
48. **If `a == b`, must `hash(a) == hash(b)`?** Yes.
49. **If `hash(a) == hash(b)`, must `a == b`?** No, that's a collision.
50. **Why are dictionaries faster than lists for the `in` operator?** Lists check every element $O(N)$; dictionaries compute the hash and look up the bucket directly $O(1)$.
51. **How do you group anagrams from a list of strings?** Sort each string and use it as a dictionary key, appending the original strings to the list value.
52. **What is the difference between `defaultdict` and `dict`?** `defaultdict` automatically initializes missing keys with a default factory (like `int` or `list`).
53. **How do you merge two dictionaries?** `dict1.update(dict2)` or `merged = {**dict1, **dict2}` or `dict1 | dict2` (Python 3.9+).
54. **What is an Ordered Map in languages like C++/Java?** A Map implemented via a Red-Black Tree, yielding $O(\log N)$ lookups but keeping keys strictly sorted.
55. **Does Python have an Ordered Map?** No standard tree-map exists. `collections.OrderedDict` only remembers insertion order, not sorted order.
56. **How to find the Kth smallest element in a BST?** Perform in-order traversal, count elements, stop at K. Time $O(H + K)$.
57. **Can we find the Kth smallest in $O(H)$ time?** Only if we augment the BST nodes to store the size of their left subtrees.
58. **How to flatten a BST into a sorted Linked List?** Modify pointers during an in-order traversal.
59. **What is the lowest common ancestor (LCA) in a BST?** Traverse from root. If both `p` and `q` are smaller, go left. If both are larger, go right. Otherwise, current is LCA.
60. **Why is LCA simpler in a BST than a normal Binary Tree?** We don't need to search both subtrees; the values dictate the exact path.
61. **How do you find the closest value to a target in a BST?** Traverse down, tracking the minimum absolute difference between the target and current node's value.
62. **What is the space complexity of checking a valid BST recursively?** $O(H)$ due to the call stack.
63. **How to construct a BST from a sorted array?** Pick the middle element as root, recursively apply to left and right halves.
64. **Why pick the middle element?** To ensure the resulting BST is height-balanced.
65. **Can a BST contain duplicate values?** Standard algorithms assume distinct values, but you can allow duplicates by placing them consistently on the left or right, or keeping a count in the node.
66. **What is a Multiset?** A Set that allows duplicate elements (can be simulated with a frequency map).
67. **How do you find duplicates in an array in $O(N)$ time and $O(1)$ space (if numbers are $1 \dots N$)?** Use the array indices themselves as a hash table, negating the value at `arr[abs(arr[i])]`.
68. **What is an Isomorphic String?** Two strings are isomorphic if characters in S can be replaced to get T. Solved using two Hash Maps.
69. **How to check for a Subarray with Sum 0?** Keep a running prefix sum and store it in a Set. If a prefix sum repeats, a zero-sum subarray exists.
70. **Why does the Prefix Sum + Hash Map technique work?** Because if $Sum_i == Sum_j$, the sum of the elements between $i$ and $j$ must be 0.
71. **How to find the Longest Consecutive Sequence in an unsorted array?** Put all numbers in a Set. For each number, if `num - 1` is not in the set, it's the start of a sequence. Count upwards.
72. **How to find the Intersection of Two Arrays II (allowing duplicates)?** Build a frequency map of the first array, then iterate through the second array, decrementing the map.
73. **What is an AVL Tree?** A strictly balanced BST where the height difference of left and right subtrees is at most 1.
74. **What is a Red-Black Tree?** A loosely balanced BST that uses coloring to ensure no path is more than twice as long as any other.
75. **Which is faster for insertions/deletions: AVL or Red-Black?** Red-Black, as it requires fewer rotations.
76. **Which is faster for lookups: AVL or Red-Black?** AVL, because it is more strictly balanced (shorter height).
77. **How do you implement a Hash Table from scratch?** Create an array of Linked Lists (or lists), compute `hash(key) % capacity` to find the bucket, and append/update the key-value pair.
78. **What is a B-Tree?** A self-balancing search tree used in databases that can have more than two children.
79. **How does hashing compare to a B-Tree for databases?** Hashing is only good for exact matches. B-Trees are required for range queries (e.g., `WHERE age > 30`).
80. **What is a Cryptographic Hash Function?** A hash function (like SHA-256) designed to be one-way, collision-resistant, and unpredictable.
81. **Why not use SHA-256 for a Hash Map?** It is computationally expensive and slow compared to simple functions like MurmurHash.
82. **How to find the maximum sum BST in a Binary Tree?** Perform post-order traversal, returning whether the subtree is a BST, its min, max, and sum.
83. **How to trim a BST given a range `[low, high]`?** Recursively drop left subtrees if node < low, or right subtrees if node > high.
84. **What is a Splay Tree?** A self-balancing BST where recently accessed elements are moved to the root, making repeated accesses $O(1)$.
85. **What is the Dutch National Flag problem?** Sorting an array of 0s, 1s, and 2s using three pointers (often done instead of a frequency map to save space).
86. **How to find pairs in two BSTs that sum to a target?** Traverse one BST and store it in a Set, then traverse the other BST and check the Set.
87. **How do you recover a BST where exactly two nodes were swapped?** Perform an in-order traversal, find the two out-of-order anomalies, and swap their values.
88. **What happens if a hash function always returns 1?** The Hash Map degrades into a Linked List ($O(N)$ lookup).
89. **How do you find the first non-repeating character in a string?** Build a frequency map, then iterate the string to find the first character with a count of 1.
90. **What is an LFU Cache and how is it related to frequency maps?** Least Frequently Used cache. It maps keys to values, and frequencies to Doubly Linked Lists of keys.
91. **What is Consistent Hashing?** A distributed hashing scheme used in load balancers and databases (like Cassandra) to minimize key movement when servers are added/removed.
92. **How to count the number of subarrays with sum K?** Keep a `prefix_sum` variable and a frequency map of prefix sums. Add `map[prefix_sum - K]` to the answer.
93. **How do you serialize a BST to an array compactly?** Pre-order traversal string.
94. **How do you determine if an array can be split into consecutive subsequences?** Use two frequency maps (one for remaining counts, one for sequence tails).
95. **What is the time complexity of deleting a leaf node in a BST?** $O(H)$ to find it, $O(1)$ to delete it.
96. **Can a Hash Map be used to detect a cycle in a Linked List?** Yes, by storing visited node references in a Set. (Though Floyd's Tortoise and Hare uses $O(1)$ space).
97. **How to find the range sum of a BST?** Traverse, only exploring the left if `root.val > low` and right if `root.val < high`.
98. **If memory is extremely constrained, Hash Map or BST?** BST (or sorted array), as Hash Maps require significant overhead for empty buckets and load factor padding.
99. **How to check if an array of strings contains duplicates?** `len(set(arr)) != len(arr)`.
100. **Why are Dictionaries, Sets, and BSTs so crucial for interviews?** Because $O(1)$ or $O(\log N)$ data retrieval is the cornerstone of optimizing naive $O(N^2)$ algorithms into passing solutions!
