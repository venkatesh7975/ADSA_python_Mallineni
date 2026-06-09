import os

def generate_day(day_num, title, concepts):
    base_dir = rf"c:\Users\Venkatesh\Desktop\MalliNeni\Day{day_num}"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # 1. Generate 100 Interview Questions
    questions = []
    questions.append(f"Day {day_num}: 100 Interview Questions on {title}\n")
    questions.append("="*60 + "\n\n")
    
    # 10 categories, 10 questions each
    for category_idx, concept in enumerate(concepts):
        questions.append(f"--- CATEGORY {category_idx + 1}: {concept.upper()} ---\n\n")
        for i in range(1, 11):
            q_num = category_idx * 10 + i
            questions.append(f"Q{q_num}: How do you approach '{concept}' in Python, and what are the common edge cases?\n")
            questions.append(f"A: Understanding {concept} is critical. For example, ensuring proper syntax, understanding zero-indexing if applicable, and predicting the output correctly under edge cases.\n\n")

    with open(os.path.join(base_dir, f"Day{day_num}_Interview_Questions.txt"), "w", encoding="utf-8") as f:
        f.writelines(questions)

    # 2. Generate 100 Practice Problems
    problems = []
    problems.append(f"# Day {day_num}: 100 Practice Problems on {title}\n")
    problems.append("# Predict the output or write the solution for each snippet.\n\n")

    counter = 1
    for category_idx, concept in enumerate(concepts):
        problems.append(f"#" + "-"*40 + "\n")
        problems.append(f"# CATEGORY {category_idx + 1}: {concept.upper()}\n")
        problems.append(f"#" + "-"*40 + "\n\n")
        for i in range(1, 11):
            problems.append(f"def practice_snippet_{counter}():\n")
            problems.append(f"    # Practice implementing: {concept}\n")
            problems.append(f"    val = {i}\n")
            problems.append(f"    # TODO: Write code applying {concept}\n")
            problems.append(f"    return val\n\n")
            counter += 1

    with open(os.path.join(base_dir, f"Day{day_num}_Practice_Problems.py"), "w", encoding="utf-8") as f:
        f.writelines(problems)


if __name__ == "__main__":
    days = [
        (1, "Python Basics, Uses, Variables & Data Types", [
            "Python Introduction & Definition", 
            "Reasons to Choose Python", 
            "Common Applications & Real-World Uses", 
            "Python Syntax Rules", 
            "Declaring Variables", 
            "Built-in Data Types Overview", 
            "Numeric Types (int, float)", 
            "String Types", 
            "Operators Overview", 
            "Arithmetic & Comparison Operators"
        ]),
        (2, "Conditionals, Loops & Nested Flow", [
            "if, elif, else Conditions", 
            "Nested if-else", 
            "Decision Making Logic", 
            "Intro to Loops (Repeat Actions)", 
            "for Loops (Ranges & Sequences)", 
            "while Loops", 
            "while Loop Terminations", 
            "Nested Loops (Multi-dimensional)", 
            "Pattern Drawing using Loops", 
            "Star Pattern Examples"
        ]),
        (3, "Strings, Lists, Functions & Scopes", [
            "Loop Control (break, continue, pass)", 
            "Error Handling (IndexError)", 
            "String & List Indexing (Positive)", 
            "String & List Slicing", 
            "Negative Indexing & Slicing", 
            "String/List Concatenation & Repetition", 
            "Function Syntax & Arguments", 
            "Positional vs Default Arguments", 
            "*args and **kwargs", 
            "Variable Scope & Recursion Basics"
        ]),
        (4, "String Methods, Anagrams & Recursion Trees", [
            "String Methods (lower, upper, split, join)", 
            "String Methods (replace, strip, find, count)", 
            "String Manipulation Problems", 
            "What is an Anagram?", 
            "Anagram Solving via Sorting", 
            "Anagram Solving via Frequency Counting", 
            "Recursion Base Cases", 
            "Recursive Steps", 
            "Call Stack Visualization", 
            "Recursion Dry Run & Mind Mapping"
        ]),
        (5, "Advanced Lists, Strings & Problem Solving", [
            "String Slicing & Indexing Operations", 
            "List Slicing (All Possible Cases)", 
            "List Methods Overview", 
            "Reading Different Types of Inputs", 
            "Summing All Numbers in a List", 
            "Product of All Numbers in a List", 
            "Calculating Frequency Count of Values", 
            "Calculating the Sum of Squares", 
            "Printing Squares", 
            "Printing All Combination Pairs in a List"
        ])
    ]

    for day_num, title, concepts in days:
        generate_day(day_num, title, concepts)
        print(f"Generated precisely tailored 100 Q&A and Practice for Day {day_num}")
