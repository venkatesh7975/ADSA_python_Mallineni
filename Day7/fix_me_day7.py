# Debugging Practice: Day 7
# Topics: Binary Search, Bubble Sort, Selection Sort, Insertion Sort
# There are 3 intentional bugs in this script. Find and fix them!

print("--- Day 7 Debugging Challenge ---")

# Bug 1: Binary Search Infinite Loop
def binary_search_buggy(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # This causes an infinite loop if target is not found!
            low = mid 
        else:
            high = mid - 1
    return -1

# Bug 2: Bubble Sort Boundaries
def bubble_sort_buggy(arr):
    n = len(arr)
    for i in range(n):
        # We should iterate up to n-i-1 to avoid IndexOutBounds and redundant checks
        for j in range(0, n - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Bug 3: Insertion Sort Shift Logic
def insertion_sort_buggy(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            # We are shifting elements, but using the wrong assignment!
            arr[j] = arr[j + 1] 
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # WARNING: This might infinite loop if not fixed!
    # print(f"1. Binary Search: {binary_search_buggy([1, 3, 5, 7, 9], 8)}")
    
    print(f"2. Bubble Sort: {bubble_sort_buggy([64, 34, 25, 12, 22, 11, 90])}")
    print(f"3. Insertion Sort: {insertion_sort_buggy([12, 11, 13, 5, 6])}")
