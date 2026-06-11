# Practice Examples: Space Complexity, Searching, and Sorting Algorithms
# Topics Covered:
# - Space Complexity Basics
# - Binary Search
# - Bubble Sort
# - Selection Sort
# - Insertion Sort

# 1. Binary Search
def binary_search(arr, target):
    """
    Searches for a target in a sorted array.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 2. Bubble Sort
def bubble_sort(arr):
    """
    Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 3. Selection Sort
def selection_sort(arr):
    """
    Sorts an array by repeatedly finding the minimum element from the unsorted part and putting it at the beginning.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 4. Insertion Sort
def insertion_sort(arr):
    """
    Builds the sorted array one item at a time by taking elements and inserting them in their correct position.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 5. Space Complexity Example (Auxiliary Space O(N))
def create_copy(arr):
    """
    Creates and returns a copy of the given array.
    Space Complexity: O(N) due to the new array created.
    """
    new_arr = arr.copy()
    return new_arr

if __name__ == "__main__":
    print("--- Binary Search ---")
    sorted_arr = [1, 3, 5, 7, 9, 11]
    print(f"Index of 7 in {sorted_arr}:", binary_search(sorted_arr, 7))

    print("\n--- Bubble Sort ---")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr1}")
    print(f"Sorted:   {bubble_sort(arr1.copy())}")

    print("\n--- Selection Sort ---")
    arr2 = [29, 10, 14, 37, 14]
    print(f"Original: {arr2}")
    print(f"Sorted:   {selection_sort(arr2.copy())}")

    print("\n--- Insertion Sort ---")
    arr3 = [12, 11, 13, 5, 6]
    print(f"Original: {arr3}")
    print(f"Sorted:   {insertion_sort(arr3.copy())}")
