# Greedy Algorithms and Techniques

## Introduction
A **Greedy Algorithm** is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are generally used for optimization problems.

An optimization problem can be solved using a Greedy approach if the problem has the following property:
At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.

## Key Characteristics
- **Greedy Choice Property:** We can make whatever choice seems best at the moment and then solve the subproblems that arise later. The choice made by a greedy algorithm may depend on choices made so far, but not on future choices or all the solutions to the subproblem. It iteratively makes one greedy choice after another, reducing each given problem into a smaller one.
- **Optimal Substructure:** A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to the sub-problems.

## Standard Greedy Algorithms
- Kruskal's Minimum Spanning Tree (MST)
- Prim's Minimum Spanning Tree
- Dijkstra's Shortest Path
- Huffman Coding

---

## Scheduling and Activity Selection

### Activity Selection Problem
The Activity Selection problem is a classic example of a problem that can be solved using a greedy approach.

**Problem Statement:**
Given a set of `n` activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

**Example:**
- Start Times: `[1, 3, 0, 5, 8, 5]`
- Finish Times: `[2, 4, 6, 7, 9, 9]`

**Greedy Approach:**
1. Sort the activities according to their finishing time.
2. Select the first activity from the sorted array and schedule it.
3. Do the following for the remaining activities in the sorted array:
   - If the start time of this activity is greater than or equal to the finish time of the previously selected activity, then select this activity.

#### Code Example (Python)
```python
def printMaxActivities(s, f):
    """
    Algorithm Steps:
    1. Assume activities are sorted by their finish times.
    2. Select the first activity (which finishes earliest).
    3. Iterate through remaining activities.
    4. If the next activity's start time >= current activity's finish time, select it.
    """
    n = len(f)
    print("Following activities are selected:")

    # Sort the activities by their finish times if not already sorted.
    # Here we assume they are already sorted by finish time for simplicity.
    # If not:
    # activities = sorted(zip(s, f), key=lambda x: x[1])
    # s = [act[0] for act in activities]
    # f = [act[1] for act in activities]

    # The first activity in the sorted list is always selected
    i = 0
    print(f"Activity 0 (Start: {s[i]}, Finish: {f[i]})")

    # Consider rest of the activities
    for j in range(1, n):
        # If this activity has start time greater than or equal to 
        # the finish time of previously selected activity, then select it
        if s[j] >= f[i]:
            print(f"Activity {j} (Start: {s[j]}, Finish: {f[j]})")
            i = j

# Driver code
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

# Function call
printMaxActivities(s, f)
```
*Time Complexity: O(N log N) if sorting is required, otherwise O(N) if already sorted.*

### Job Sequencing Problem
**Problem Statement:**
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. Maximize the total profit if only one job can be scheduled at a time.

**Greedy Approach:**
1. Sort all jobs in decreasing order of profit.
2. Initialize the result sequence and a time slot array to keep track of free time slots.
3. Iterate through the sorted jobs:
   - For each job, find a free time slot starting from its deadline down to 1.
   - If a free slot is found, schedule the job in that slot.

### Fractional Knapsack Problem
**Problem Statement:**
Given weights and values of `n` items, we need to put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.

**Greedy Approach:**
1. Calculate the ratio (`value/weight`) for each item.
2. Sort the items based on this ratio in descending order.
3. Take the item with the highest ratio and add them until we can't add the next item as a whole.
4. At the end, add the next item as much (fractional part) as we can to exactly fill the knapsack.

---

## Simple LeetCode Problems

### 1. Assign Cookies (LeetCode 455)
**Problem:**
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Greedy Approach:**
Sort both arrays (children's greed and cookie sizes). Use a two-pointer approach to match the smallest available cookie to the child with the smallest greed that it can satisfy.

**Python Solution:**
```python
def findContentChildren(g, s):
    """
    Algorithm Steps:
    1. Sort the children's greed factors (g).
    2. Sort the available cookie sizes (s).
    3. Use two pointers to check each cookie against the least greedy child.
    4. If cookie size >= child's greed, assign it and move to next child.
    5. Always move to next cookie.
    """
    g.sort()
    s.sort()
    
    child_i = 0
    cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            # Cookie is large enough to satisfy the child
            child_i += 1
        # Always move to the next cookie
        cookie_j += 1
        
    return child_i
```

### 2. Best Time to Buy and Sell Stock II (LeetCode 122)
**Problem:**
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

**Greedy Approach:**
Since we know the prices for each day, we can greedily capture every single profit possible. If the price tomorrow is higher than the price today, we pretend we bought it today and sold it tomorrow. This accumulates all positive price differences.

**Python Solution:**
```python
def maxProfit(prices):
    """
    Algorithm Steps:
    1. Initialize total profit to 0.
    2. Loop through the array of prices starting from day 2 (index 1).
    3. If the price today is higher than yesterday, add the difference to profit.
    4. Return the accumulated profit.
    """
    profit = 0
    for i in range(1, len(prices)):
        # If the price goes up, we take the profit
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

### 3. Maximum 69 Number (LeetCode 1323)
**Problem:**
You are given a positive integer `num` consisting only of digits 6 and 9. Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

**Greedy Approach:**
To maximize the number, we should greedily change the most significant (leftmost) digit that is a '6' into a '9'. If all digits are already '9', we don't change anything.

**Python Solution:**
```python
def maximum69Number(num):
    """
    Algorithm Steps:
    1. Convert the integer into a string/list of characters to iterate.
    2. Traverse from left to right (most significant digit to least).
    3. At the first encounter of '6', change it to '9'.
    4. Break out of the loop and return the converted integer.
    """
    # Convert number to a list of characters for easy modification
    num_str = list(str(num))
    
    # Greedily change the first '6' to '9'
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str[i] = '9'
            break
            
    return int("".join(num_str))
```

### 4. Shortest Job First (SJF) CPU Scheduling
**Problem:**
Shortest Job First (SJF) is a scheduling policy that selects the waiting process with the smallest execution time (burst time) to execute next. Given an array of processes where each process has a unique ID and a burst time, the goal is to find the average waiting time and average turnaround time using the non-preemptive SJF algorithm. For simplicity, assume all processes arrive at time 0.

**Greedy Approach:**
If all processes arrive at the same time, the greedy strategy is to simply sort the processes by their burst time in ascending order. We then schedule the jobs one by one. By executing the shortest job first, we minimize the accumulated waiting time for all subsequent jobs, thereby minimizing the average waiting time overall.

**Python Solution (Assuming all arrive at time 0):**
```python
def sjf_scheduling(processes, burst_times):
    """
    Algorithm Steps:
    1. Pair each process ID with its corresponding burst time.
    2. Sort these pairs in ascending order based on burst times.
    3. Initialize waiting time for the first process as 0.
    4. For subsequent processes, Waiting Time = Previous Process Waiting Time + Previous Process Burst Time.
    5. Turnaround Time = Waiting Time + Burst Time.
    6. Calculate and print the averages.
    """
    n = len(processes)
    # Combine process IDs with their burst times and sort by burst time
    jobs = list(zip(processes, burst_times))
    jobs.sort(key=lambda x: x[1])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Waiting time for first process is 0
    waiting_time[0] = 0
    turnaround_time[0] = jobs[0][1]
    
    # Calculate waiting time and turnaround time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + jobs[i-1][1]
        turnaround_time[i] = waiting_time[i] + jobs[i][1]
        
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    print("Process ID | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"    {jobs[i][0]}      |     {jobs[i][1]}      |      {waiting_time[i]}       |        {turnaround_time[i]}")
        
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example Usage:
# processes = [1, 2, 3, 4]
# burst_times = [6, 8, 7, 3]
# sjf_scheduling(processes, burst_times)
```

### 5. Shortest Remaining Time First (SRTF) - Preemptive SJF
**Problem:**
Shortest Remaining Time First (SRTF) is the preemptive version of SJF. In this problem, processes have varying **arrival times** and **burst times**. If a new process arrives with a shorter burst time than the remaining burst time of the currently executing process, the CPU is preempted (taken away) from the current process and allocated to the new one. 

**Greedy Approach:**
At every unit of time (or whenever a new process arrives/a process finishes), we greedily evaluate all the processes that have already arrived and have not yet completed. We pick the one with the **minimum remaining burst time**. This ensures that shorter jobs finish as quickly as possible, which minimizes overall average waiting time.

**Python Solution:**
```python
def srtf_scheduling(processes, arrival_times, burst_times):
    """
    Algorithm Steps:
    1. Create an array to track remaining burst times for all processes.
    2. Maintain a `current_time` counter starting at 0.
    3. In a loop, find the process that has arrived (arrival time <= current_time) 
       AND has the minimum remaining burst time > 0.
    4. Execute this process for 1 unit of time (decrement its remaining time).
    5. If a process finishes (remaining time == 0), calculate its completion, turnaround, and waiting times.
    6. Repeat until all processes are complete.
    """
    n = len(processes)
    # Store remaining times
    remaining_times = list(burst_times)
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    complete = 0
    current_time = 0
    min_remaining = float('inf')
    shortest = 0
    check = False
    
    # Run until all processes are complete
    while complete != n:
        
        # Find process with minimum remaining time among arrived processes
        for j in range(n):
            if ((arrival_times[j] <= current_time) and 
                (remaining_times[j] < min_remaining) and 
                remaining_times[j] > 0):
                min_remaining = remaining_times[j]
                shortest = j
                check = True
                
        if not check:
            # If no process has arrived yet, just advance time
            current_time += 1
            continue
            
        # Execute shortest process for 1 time unit
        remaining_times[shortest] -= 1
        
        # Update minimum
        min_remaining = remaining_times[shortest]
        if min_remaining == 0:
            min_remaining = float('inf')
            
        # If a process gets completely executed
        if remaining_times[shortest] == 0:
            complete += 1
            check = False
            
            # Completion time of current process
            finish_time = current_time + 1
            
            # Calculate waiting time: Wait Time = Turnaround Time - Burst Time
            # Turnaround Time = Finish Time - Arrival Time
            turnaround_time[shortest] = finish_time - arrival_times[shortest]
            waiting_time[shortest] = turnaround_time[shortest] - burst_times[shortest]
            
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0
        
        # Increment time
        current_time += 1
        
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    print("PID | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f" {processes[i]}  |      {arrival_times[i]}       |     {burst_times[i]}      |      {waiting_time[i]}       |       {turnaround_time[i]}")
        
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example Usage:
# processes = [1, 2, 3, 4]
# arrival_times = [0, 1, 2, 3]
# burst_times = [8, 4, 9, 5]
# srtf_scheduling(processes, arrival_times, burst_times)
```
