#student Self Review assessment form: https://forms.gle/tdaJntw6URM8xwkeA

#Mock Interview Form: https://forms.gle/2FYhboNRzDPjU8Gt7

##Test Feedback for Bytexl: https://forms.gle/Z5sg5JPb1q6DBjhj9

# Git Setup & Push Commands

## Configure Git Username

```bash
git config --global user.name "githubusername"
```

Example:

```bash
git config --global user.name "venkatesh7975"
```

---

## Configure Git Email

```bash
git config --global user.email "gitemail"
```

Example:

```bash
git config --global user.email "yourmail@gmail.com"
```

---

## Verify Configuration

```bash
git config --global --list
```

---

## Remove Existing Remote

```bash
git remote remove origin
```

---

# Push Local Project to GitHub

## Initialize Git Repository

```bash
git init
```

## Add All Files

```bash
git add .
```

## Create Commit

```bash
git commit -m "Initial commit"
```

## Rename Branch to Main

```bash
git branch -M main
```

## Add GitHub Repository

```bash
git remote add origin repository-url
```

Example:

```bash
git remote add origin https://github.com/username/repository-name.git
```

## Push Code to GitHub

```bash
git push -u origin main
```

---

# Check Connected Remote Repository

```bash
git remote -v
```

---

# Clone Existing Repository

```bash
git clone repository-url
```

Example:

```bash
git clone https://github.com/username/repository-name.git
```

---

# Pull Latest Changes

```bash
git pull origin main
```

---

# Push New Changes

```bash
git add .
git commit -m "Updated project"
git push origin main
```

---

# Useful Git Commands

## Check Status

```bash
git status
```

## View Commit History

```bash
git log --oneline
```

## Create New Branch

```bash
git checkout -b branch-name
```

## Switch Branch

```bash
git checkout branch-name
```

## Merge Branch

```bash
git merge branch-name
```




## 🔗 Important Program Links
- **Daily Quiz Link:** Day13: https://forms.gle/eqS9nVHZCpRuRHXA8
- **Daily Feedback Form:** [Submit Feedback](https://forms.gle/cg1ipBgTk3aHcaFm6)
- **Student Profiles Form:** [Update Profile](https://forms.gle/vETWosRivXR6s2Ro6)
- **Practice Problems Reference:** [GeeksforGeeks](https://www.geeksforgeeks.org/c/c-programming-examples/)
- **DSA sheet :** https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z


## 📝 Daily LinkedIn Post AI Prompt Template
*Copy and paste the prompt below into ChatGPT/Gemini to generate a viral-worthy LinkedIn post for your daily updates.*

> **Prompt:**
> "I am participating in a 30-Day Coding Challenge. Today is **Day [Insert Day Number]**, and I learned and implemented **[Insert Topic, e.g., Circular Queues and Deques]**. I successfully solved problems such as **[Insert Problem Names]**. 
> 
> Please write an engaging, highly professional, and inspiring LinkedIn post to share my progress. My target audience includes top-tier tech recruiters and engineers (aiming for premium software engineering roles). The post should be optimized to reach maximum impressions (1000/1000 quality).
> 
> Include:
> 1. A catchy hook.
> 2. 2-3 key technical takeaways from today's topic.
> 3. Clean formatting with bullet points and emojis.
> 4. Appropriate trending hashtags (e.g., #30DaysOfCode, #DataStructures, #Python, #SoftwareEngineering).
> 5. A call-to-action (CTA) asking my network a related technical question to drive engagement in the comments."

---


---

# Python Mastery Course (7 Days to Algorithms)

Welcome to the **Python Mastery Course**, a comprehensive curriculum designed to take you from absolute zero to writing optimized searching algorithms.

This repository is structured by day. Each day acts as a progressive module complete with Class Notes, Interactive Examples, 100 Interview Questions, 100 Practice Problems, and beautiful UI notes.

---

## 📚 General References
- **[Introduction to Data Structures](Data_Structures_Overview.md)**: A high-level overview of what Data Structures are, along with the different primitive, linear, and non-linear types.
- **[Data Structures Interview Questions](Data_Structures_Interview_Questions.md)**: 15 essential interview questions and answers covering general Data Structures and Queues.

## 📚 Interview Question Banks
- **[Python Core Concepts](./python_core_concepts.md)**: Basics, Syntax, Data Types, Control Flow, Scope, Error Handling.
- **[Python Advanced Concepts](./python_advanced_concepts.md)**: OOP, Iterators, Generators, Decorators, Memory Management, Concurrency.
- **[DSA - Data Structures](./dsa_data_structures.md)**: Arrays, Strings, Linked Lists, Stacks, Queues, Hash Tables, Trees, Graphs, Heaps.
- **[DSA - Algorithms](./dsa_algorithms.md)**: Sorting, Searching, Dynamic Programming, Greedy Algorithms, Graph Traversals, Backtracking.
- **[System Design & Ecosystem](./system_design_and_best_practices.md)**: Design Patterns, REST APIs, CAP Theorem, Scaling, Caching, Python Ecosystem.

## 🚀 Best Free Public Resources

### 🐍 Learn Python (Beginner to Advanced)
- **[Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)**
- **[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)**
- **[Corey Schafer's Python Tutorials (YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)**
- **[Real Python](https://realpython.com/)**

### 🧠 Learn Data Structures & Algorithms (Language Agnostic)
- **[MIT OpenCourseWare - 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)**
- **[BaseCS](https://medium.com/basecs)**
- **[Coursera - Algorithms Specialization (Stanford)](https://www.coursera.org/specializations/algorithms)**

### 🛠️ Learn DSA Specifically in Python
- **[Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)**
- **[NeetCode (YouTube & Website)](https://neetcode.io/)**
- **[The Algorithms - Python (GitHub)](https://github.com/TheAlgorithms/Python)**

### 💻 Practice Platforms
- **[LeetCode](https://leetcode.com/)**
- **[HackerRank](https://www.hackerrank.com/domains/python)**

## 📚 Curriculum Flow

### Day 1: Python Basics & Variables
- Syntax, numeric datatypes (int, float), string types, and basic operators.

### Day 2: Conditionals & Loops
- If-else statements, basic logic, for-loops, while-loops, and nested loops (Star Patterns).

### Day 3: Strings, Lists & Functions
- Loop controls, list/string slicing, positive/negative indexing, and custom function definitions.

### Day 4: Advanced Data & Recursion
- String methods, solving anagrams (sorting vs frequency counting), and an introduction to recursive logic trees.

### Day 5: Problem Solving Strategies
- Iterating through lists to find sums, products, combinations, and counting frequencies.

### Day 6: Time & Space Complexity (Big O Notation)
- The language of performance. Understanding O(1), O(N), O(N^2), O(N log N), and Space Complexity.
- Includes LeetCode Practice Tasks targeting Time Complexity optimization (e.g., Two Sum, Count Primes).

### Day 7: Searching Algorithms
- Translating theoretical Big O into practice: The slow O(N) Linear Search vs the incredibly fast O(log N) Binary Search.

### Day 8: Basic Sorting & Recursion
- Deep dive into Recursion logic.
- Fundamental sorting algorithms: **Bubble Sort**, **Selection Sort**, and **Insertion Sort**.

### Day 9: Sorting Algorithms & Visualizer Academy
- Deep dive into **Merge Sort** and **Quick Sort**.
- Explore the **[God-Level Sorting Visualizer Academy](https://sorting-visualizer-academy.vercel.app)** built to perfectly trace recursive trees, call stacks, and array partitioning interactively.

### Day 10: Introduction to Stacks
- The LIFO Principle (Last In, First Out).
- Core Operations: Push, Pop, Peek.
- Using Python's built-in `list` to achieve O(1) time complexity.
- Applications: Simulation, Validating Parentheses, and Monotonic Sequences.

### Day 11: Mastery of Stacks and Queues
- Deep dive into both the LIFO (Stack) and FIFO (Queue) principles.
- Comprehensive Python implementations: `list`, `collections.deque`, `queue.Queue`, Priority Queues, and Circular Queues.
- **20 Classic LeetCode Problems** fully solved (including Monotonic Stacks and Deques).
- Explore the **Interactive Valid Parentheses Visualizer**, a premium React web app built to animate O(1) stack evaluations in real-time.

### Day 12: Circular Queues and Deques
- Special queue variants: Circular Queues (Ring Buffers) and Deques (Double Ended Queues).
- Operations and implementation mechanics (Modulo arithmetic, Array scaling).
- Complete Python representations of Circular Queues using both Arrays and purely Linked Lists.
- Real-world algorithms: Sliding Window Maximum and Palindrome verification.

### Day 13: Linked Lists Algorithm Mastery
- Focus on pointer manipulation and traversal techniques.
- Algorithms implemented: Two-pointer technique (Fast & Slow pointers), Floyd's Tortoise and Hare.
- Classic LeetCode solutions: Reverse Linked List, Merge Sorted Lists, Cycle Detection, and Nth Node Removal.

### Day 14: Introduction to Trees & BSTs
- Hierarchical data structures and recursive thinking.
- Binary Trees vs. Binary Search Trees.
- DFS Traversals (Inorder, Preorder, Postorder) and BFS Traversals (Level-order).
- 50 optimal Python solutions to core LeetCode Tree problems (LCA, Validation, Subtrees, Path Sums).

### Day 15: Hashing, Sets & BST Advanced Problem Solving
- Deep dive into $O(1)$ Hash Map implementations, Load Factors, and Collisions.
- Mastering Frequency Maps (`Counter`) and Sets for uniqueness and $O(N)$ speedups.
- Integrating Sets with Prefix Sums and BST traversals.
- 50 elite LeetCode problems solved (Two Sum variations, Group Anagrams, Subarray Sums).

---
*Built with ❤️ for rapid Python proficiency.*
