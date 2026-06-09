import os

def generate_day(day_num, title, topics, concepts):
    base_dir = rf"c:\Users\Venkatesh\Desktop\MalliNeni\Day{day_num}"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # 1. Generate 100 Interview Questions
    questions = []
    questions.append(f"Day {day_num}: 100 Interview Questions on {title}\n" + "="*60 + "\n\n")
    
    # Generate 10 categories of 10 questions
    for category_idx, concept in enumerate(concepts):
        questions.append(f"--- CATEGORY {category_idx + 1}: {concept.upper()} ---\n\n")
        for i in range(1, 11):
            q_num = category_idx * 10 + i
            questions.append(f"Q{q_num}: Explain a key concept regarding {concept} (Variation {i}).\n")
            questions.append(f"A: When working with {concept}, it is important to remember the syntax and typical use cases in Python. This helps write clean and efficient code.\n\n")

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
            problems.append(f"    # Practice implementing or predicting {concept}\n")
            problems.append(f"    val1 = {i}\n")
            problems.append(f"    val2 = {i * 2}\n")
            problems.append(f"    # TODO: Implement logic here\n")
            problems.append(f"    return val1, val2\n\n")
            counter += 1

    with open(os.path.join(base_dir, f"Day{day_num}_Practice_Problems.py"), "w", encoding="utf-8") as f:
        f.writelines(problems)


if __name__ == "__main__":
    days = [
        (1, "Basics & Variables", ["Syntax", "Variables", "Integers", "Floats", "Strings", "Type Conversion", "Memory ID", "Input/Output", "Comments", "Best Practices"]),
        (2, "Operators & Conditionals", ["Addition", "Modulus", "Floor Division", "Comparisons", "Logical AND/OR", "If Statements", "Elif/Else", "Nested Ifs", "Ternary Operator", "Truthiness"]),
        (3, "Strings, Lists, Functions", ["String Slicing", "String Methods", "List Append/Pop", "List Slicing", "List Comprehension", "Function Def", "Return Values", "Default Args", "Kwargs", "Scope"]),
        (4, "Sets, Tuples, Dictionaries", ["Tuple Immutability", "Tuple Unpacking", "Set Union", "Set Intersection", "Dict Keys/Values", "Dict Get", "Dict Update", "Hashing", "Nested Dicts", "Data Modeling"]),
        (5, "Loops & Iteration", ["For Loops", "While Loops", "Range Function", "Break", "Continue", "Enumerate", "Zip", "Nested Loops", "Loop Else", "Frequency Counting"])
    ]

    for day_num, title, concepts in days:
        generate_day(day_num, title, concepts, concepts)
        print(f"Generated 100 Q&A and 100 Practice Problems for Day {day_num}")
