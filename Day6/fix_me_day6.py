# Debugging Practice: Day 6
# Topics: Big O Time Complexity, Linear Search
# There are 3 intentional bugs/inefficiencies in this script. Find and fix them!

print("--- Day 6 Debugging Challenge ---")

# Bug 1: Linear Search Logic
def linear_search_buggy(arr, target):
    # We want to return the index if found, else -1
    for i in range(len(arr)):
        if arr[i] == target:
            return True # Should return the index, not a boolean!
    return False

# Bug 2: O(N^2) inefficiency in what should be an O(N) loop
def find_duplicates_inefficient(arr):
    # We want to find duplicates. 
    # Calling .count() inside a loop makes this O(N^2) instead of O(N)
    duplicates = []
    for item in arr:
        if arr.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Bug 3: Finding Max element
def find_max_buggy(arr):
    # We want to find the maximum element in O(N)
    if not arr: return None
    
    max_val = 0 # What if all numbers in the array are negative?
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == "__main__":
    print(f"1. Linear Search for 5: {linear_search_buggy([1, 2, 3, 4, 5], 5)}")
    print(f"2. Duplicates: {find_duplicates_inefficient([1, 2, 3, 1, 2, 4])}")
    print(f"3. Max in negative array: {find_max_buggy([-10, -20, -5, -30])}")
