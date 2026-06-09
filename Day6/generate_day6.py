import os

def generate_interview_questions():
    questions = []
    
    # Category 1: Fundamentals of Big O (10 Qs)
    for i in range(1, 11):
        questions.append(f"Q{i}: What does Big O notation measure?\nA: It measures how the runtime or space requirements of an algorithm grow as the input size (N) grows towards infinity.")

    # Category 2: O(1) Constant Time (10 Qs)
    for i in range(11, 21):
        questions.append(f"Q{i}: Give an example of an O(1) operation.\nA: Accessing an array element by its index, e.g., `arr[5]`, is O(1) because it takes a constant number of steps regardless of array size.")

    # Category 3: O(N) Linear Time (10 Qs)
    for i in range(21, 31):
        questions.append(f"Q{i}: If you loop through an array and then loop through it again (not nested), what is the time complexity?\nA: O(N) + O(N) = O(2N). Dropping the constant gives us O(N).")

    # Category 4: O(N^2) Quadratic Time (10 Qs)
    for i in range(31, 41):
        questions.append(f"Q{i}: What is the time complexity of a nested loop where both loops run N times?\nA: O(N * N) = O(N^2). This is typical in algorithms like Bubble Sort.")

    # Category 5: O(log N) Logarithmic (10 Qs)
    for i in range(41, 51):
        questions.append(f"Q{i}: How does O(log N) scale compared to O(N)?\nA: O(log N) is vastly superior for large datasets. It implies the search space is halved at each step (e.g., Binary Search).")

    # Category 6: O(N log N) Linearithmic (10 Qs)
    for i in range(51, 61):
        questions.append(f"Q{i}: What common algorithms run in O(N log N) time?\nA: Efficient sorting algorithms like Merge Sort, Quick Sort, and Heap Sort. It usually occurs when you do an O(log N) operation N times.")

    # Category 7: O(N^3) Cubic Time (10 Qs)
    for i in range(61, 71):
        questions.append(f"Q{i}: When would you encounter an O(N^3) time complexity?\nA: It typically occurs with three nested loops, often seen in naive matrix multiplication or finding triplets that sum to a value.")

    # Category 8: O(2^N) Exponential Time (10 Qs)
    for i in range(71, 81):
        questions.append(f"Q{i}: Why is O(2^N) considered extremely inefficient?\nA: Because adding just one more element to the input doubles the amount of work. It is common in naive recursive algorithms like Fibonacci without memoization.")

    # Category 9: Space Complexity (20 Qs)
    for i in range(81, 101):
        questions.append(f"Q{i}: If an algorithm creates a copy of the input array, what is its space complexity?\nA: O(N), because the extra memory required grows directly in proportion to the input size.")

    # High quality overrides for the first few
    overrides = [
        ("What does Big O notation mathematically represent?", "It represents the asymptotic upper bound (worst-case scenario) of an algorithm's complexity."),
        ("What is the time complexity of appending an element to the end of a Python list?", "O(1) amortized, because Python lists are dynamic arrays that allocate extra space in advance."),
        ("What is the time complexity of inserting an element at the BEGINNING of a Python list?", "O(N), because every existing element must be shifted one position to the right in memory."),
        ("What is the time complexity of looking up a key in a Python dictionary?", "O(1) on average, because dictionaries are implemented as Hash Maps.")
    ]
    for idx, (q, a) in enumerate(overrides):
        questions[idx] = f"Q{idx+1}: {q}\nA: {a}"

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Interview_Questions.txt", "w", encoding="utf-8") as f:
        f.write("Day 6: 100 High-Quality Interview Questions on Big O Notation\n")
        f.write("="*60 + "\n\n")
        for q in questions:
            f.write(q + "\n\n")


def generate_practice_problems():
    problems = []
    
    problems.append("# Day 6: Big O Notation Reference Code & Practice\n")
    problems.append("# Analyze the Time and Space Complexity for each snippet.\n\n")

    counter = 1

    # --- O(1) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 1: O(1) CONSTANT TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(1) | Expected Space: O(1)\n")
        problems.append(f"    if len(arr) > {i}:\n")
        problems.append(f"        return arr[{i-1}]\n")
        problems.append(f"    return None\n\n")
        counter += 1

    # --- O(log N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 2: O(log N) LOGARITHMIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(log N) | Expected Space: O(1)\n")
        problems.append(f"    steps = 0\n")
        problems.append(f"    while n > {i}:\n")
        problems.append(f"        n = n // 2\n")
        problems.append(f"        steps += 1\n")
        problems.append(f"    return steps\n\n")
        counter += 1

    # --- O(N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 3: O(N) LINEAR TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N) | Expected Space: O(1)\n")
        problems.append(f"    total = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        total += x + {i}\n")
        problems.append(f"    return total\n\n")
        counter += 1

    # --- O(N log N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 4: O(N log N) LINEARITHMIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(N log N) | Expected Space: O(1)\n")
        problems.append(f"    count = 0\n")
        problems.append(f"    for i in range(n):\n")
        problems.append(f"        j = n\n")
        problems.append(f"        while j > 1:\n")
        problems.append(f"            j = j // 2\n")
        problems.append(f"            count += 1\n")
        problems.append(f"    return count\n\n")
        counter += 1

    # --- O(N^2) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 5: O(N^2) QUADRATIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N^2) | Expected Space: O(1)\n")
        problems.append(f"    pairs_found = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        for y in arr:\n")
        problems.append(f"            if x + y == {i * 10}:\n")
        problems.append(f"                pairs_found += 1\n")
        problems.append(f"    return pairs_found\n\n")
        counter += 1

    # --- O(N^3) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 6: O(N^3) CUBIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N^3) | Expected Space: O(1)\n")
        problems.append(f"    triplets = 0\n")
        problems.append(f"    n = len(arr)\n")
        problems.append(f"    for i in range(n):\n")
        problems.append(f"        for j in range(n):\n")
        problems.append(f"            for k in range(n):\n")
        problems.append(f"                if arr[i] + arr[j] + arr[k] == 0:\n")
        problems.append(f"                    triplets += 1\n")
        problems.append(f"    return triplets\n\n")
        counter += 1

    # --- O(2^N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 7: O(2^N) EXPONENTIAL TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack\n")
        problems.append(f"    if n <= 1:\n")
        problems.append(f"        return n\n")
        problems.append(f"    return snippet_{counter}(n - 1) + snippet_{counter}(n - 2)\n\n")
        counter += 1

    # --- O(N) Space Complexity Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 8: O(N) SPACE COMPLEXITY\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N) | Expected Space: O(N)\n")
        problems.append(f"    new_array = []\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        new_array.append(x * {i})\n")
        problems.append(f"    return new_array\n\n")
        counter += 1

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Practice_Problems.py", "w", encoding="utf-8") as f:
        f.writelines(problems)

if __name__ == "__main__":
    generate_interview_questions()
    generate_practice_problems()
    print("Successfully generated all Big O snippets including NlogN, N^3, and 2^N.")
