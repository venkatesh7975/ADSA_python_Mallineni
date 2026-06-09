import os
import random

def generate_day1_problems():
    problems = []
    for i in range(1, 51):
        category = i % 5
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        if category == 0:
            q = f"Create a variable `x` with value {n1} and `y` with value {n2}. Print their sum."
            a = f"x = {n1}\ny = {n2}\nprint(x + y)"
        elif category == 1:
            q = f"Calculate the remainder of {n1} divided by {random.randint(2, 10)}."
            divisor = random.randint(2, 10)
            a = f"print({n1} % {divisor})"
        elif category == 2:
            q = f"Convert the float `{n1}.5` to an integer and print it."
            a = f"print(int({n1}.5))"
        elif category == 3:
            word1 = random.choice(["Hello", "Python", "Data", "Code"])
            word2 = random.choice(["World", "Rocks", "Science", "Base"])
            q = f"Concatenate '{word1}' and '{word2}' with a space in between."
            a = f'print("{word1}" + " " + "{word2}")'
        else:
            q = f"Check if {n1} is strictly greater than {n2} and print the boolean result."
            a = f"print({n1} > {n2})"
        problems.append((q, a))
    return problems

def generate_day2_problems():
    problems = []
    for i in range(1, 51):
        category = i % 4
        n1 = random.randint(5, 15)
        if category == 0:
            q = f"Write a for loop that prints numbers from 0 to {n1 - 1}."
            a = f"for i in range({n1}):\n    print(i)"
        elif category == 1:
            q = f"Write an if-else statement that prints 'Even' if {n1} is even, else 'Odd'."
            a = f"n = {n1}\nif n % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')"
        elif category == 2:
            word = random.choice(["Python", "Loop", "Code"])
            q = f"Use a while loop to print '{word}' {n1 % 5 + 2} times."
            times = n1 % 5 + 2
            a = f"count = 0\nwhile count < {times}:\n    print('{word}')\n    count += 1"
        else:
            q = f"Print numbers from 1 to 10 but `break` the loop if the number equals {n1 % 5 + 3}."
            stop = n1 % 5 + 3
            a = f"for i in range(1, 11):\n    if i == {stop}:\n        break\n    print(i)"
        problems.append((q, a))
    return problems

def generate_day3_problems():
    problems = []
    for i in range(1, 51):
        category = i % 5
        n1 = random.randint(1, 20)
        n2 = random.randint(21, 40)
        if category == 0:
            q = f"Create a list with numbers {n1}, {n2}, and {n1+n2}. Print the list."
            a = f"lst = [{n1}, {n2}, {n1+n2}]\nprint(lst)"
        elif category == 1:
            q = f"Write a function `multiply(a, b)` that returns the product of a and b. Call it with {n1} and {n2}."
            a = f"def multiply(a, b):\n    return a * b\n\nprint(multiply({n1}, {n2}))"
        elif category == 2:
            q = f"Append the number {n1} to the list `[1, 2, 3]` and print it."
            a = f"lst = [1, 2, 3]\nlst.append({n1})\nprint(lst)"
        elif category == 3:
            q = f"Write a function that takes `*args` and returns the sum of all arguments."
            a = f"def sum_all(*args):\n    return sum(args)\n\nprint(sum_all(1, 2, 3))"
        else:
            q = f"Extract the first two elements from the list `[10, 20, 30, 40]` using slicing."
            a = f"lst = [10, 20, 30, 40]\nprint(lst[:2])"
        problems.append((q, a))
    return problems

def generate_day4_problems():
    problems = []
    for i in range(1, 51):
        category = i % 4
        n1 = random.randint(1, 5)
        if category == 0:
            word = random.choice(["python", "recursion", "anagram", "code"])
            q = f"Convert the string '{word}' to uppercase and print it."
            a = f"s = '{word}'\nprint(s.upper())"
        elif category == 1:
            q = f"Write a recursive function to print numbers from {n1} down to 1."
            a = f"def count_down(n):\n    if n <= 0:\n        return\n    print(n)\n    count_down(n - 1)\n\ncount_down({n1})"
        elif category == 2:
            word1 = random.choice(["listen", "rat", "evil"])
            word2 = random.choice(["silent", "tar", "vile"])
            q = f"Check if '{word1}' and '{word2}' are anagrams by sorting them."
            a = f"w1, w2 = '{word1}', '{word2}'\nprint(sorted(w1) == sorted(w2))"
        else:
            q = f"Count how many times the letter 'a' appears in 'banana'."
            a = f"s = 'banana'\nprint(s.count('a'))"
        problems.append((q, a))
    return problems

def html_for_problems(problems):
    html = f'''
        <section class="glass-card">
            <h2>50 Practice Problems & Solutions</h2>
            <p>Master the daily topics with these 50 quick exercises!</p>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1rem;">
'''
    for i, (q, a) in enumerate(problems, 1):
        html += f'''
                <div style="background: rgba(255, 255, 255, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong>Q{i}: {q}</strong>
                    <details style="color: var(--accent-1); cursor: pointer; margin-top: 0.5rem;">
                        <summary>View Solution</summary>
                        <pre style="margin-top: 0.5rem;"><code style="color: #a6e22e;">{a}</code></pre>
                    </details>
                </div>
'''
    html += '''
            </div>
        </section>

        <section class="glass-card">
            <h2>Resources & Practice</h2>
'''
    return html

def inject_into_file(filepath, problems):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = '''        </section>

        <section class="glass-card">
            <h2>Resources & Practice</h2>'''
    
    if target in content:
        content = content.replace(target, html_for_problems(problems))
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"Target string not found in {filepath}")

def main():
    base_dir = r"c:\\Users\\Venkatesh\\Desktop\\MalliNeni"
    
    inject_into_file(os.path.join(base_dir, "Day1", "blog.html"), generate_day1_problems())
    inject_into_file(os.path.join(base_dir, "Day2", "blog.html"), generate_day2_problems())
    inject_into_file(os.path.join(base_dir, "Day3", "blog.html"), generate_day3_problems())
    inject_into_file(os.path.join(base_dir, "Day4", "blog.html"), generate_day4_problems())

if __name__ == "__main__":
    main()
