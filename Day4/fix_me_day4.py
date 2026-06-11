# Debugging Practice: Day 4
# Topics: String Methods, Anagrams, Recursion
# There are 4 intentional bugs in this script. Find and fix them!

print("--- Day 4 Debugging Challenge ---")

# Bug 1: Method not called
def format_title(title):
    # We want to make the title uppercase
    return title.upper

# Bug 2: Anagram frequency logic
def is_anagram_buggy(str1, str2):
    # We want to count frequencies using a dictionary
    freq1 = {}
    for char in str1:
        # dicts don't have an append method!
        freq1.append(char)
    return freq1

# Bug 3: String slicing error
def get_middle_chars():
    word = "python"
    # We want to extract "th"
    # Remember slicing is [start:stop] where stop is exclusive
    mid = word[2:3]
    return mid

# Bug 4: Recursion logic
def factorial_buggy(n):
    # Factorial base case is 0! = 1 or 1! = 1
    if n == 0:
        return 0
    return n * factorial_buggy(n - 1)

if __name__ == "__main__":
    print(f"1. Formatted Title: {format_title('hello world')}")
    
    try:
        print(f"2. Anagram Check: {is_anagram_buggy('listen', 'silent')}")
    except Exception as e:
        print(f"2. Error: {e}")
        
    print(f"3. Middle Chars: {get_middle_chars()}")
    print(f"4. Factorial of 5: {factorial_buggy(5)}")
