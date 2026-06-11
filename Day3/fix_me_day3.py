# Debugging Practice: Day 3
# Topics: Strings, Lists, Loop Control, Functions, Scope, Recursion
# There are 5 intentional bugs in this script. Find and fix them!

print("--- Day 3 Debugging Challenge ---")

# Bug 1: Strings are immutable
def fix_greeting():
    greeting = "Hillo"
    # We want to change 'i' to 'e'
    greeting[1] = 'e'
    print(f"1. Greeting: {greeting}")

# Bug 2: List out of bounds
def get_last_item():
    my_list = [10, 20, 30]
    # We want to print the last item (30)
    print(f"2. Last item: {my_list[3]}")

# Bug 3: Scope issue
def calculate_total():
    total = 0
    for i in range(5):
        total = total + i
    # We want to print the final total outside the loop
    print(f"3. Total: {i}")

# Bug 4: Missing base case causing infinite recursion
def countdown(n):
    print(n)
    countdown(n - 1)

# Bug 5: Loop control logic error
def find_even():
    # We want to print the first even number and then stop
    nums = [1, 3, 5, 8, 9, 10]
    for n in nums:
        if n % 2 == 0:
            print(f"5. Found first even: {n}")
            continue

if __name__ == "__main__":
    try: fix_greeting()
    except Exception as e: print(f"1. Error: {e}")
    
    try: get_last_item()
    except Exception as e: print(f"2. Error: {e}")
    
    try: calculate_total()
    except Exception as e: print(f"3. Error: {e}")
    
    # countdown(5) # Uncomment when fixed!
    
    try: find_even()
    except Exception as e: print(f"5. Error: {e}")
