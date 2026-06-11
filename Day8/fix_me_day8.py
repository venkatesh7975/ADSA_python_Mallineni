# Debugging Practice: Day 8
# Topics: Merge Sort, Quick Sort
# There are 2 intentional bugs in this script. Find and fix them!

print("--- Day 8 Debugging Challenge ---")

# Bug 1: Merge Sort Merging Logic
def merge_sort_buggy(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_buggy(L)
        merge_sort_buggy(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            # Sort in ascending order
            if L[i] > R[j]: # This condition is flipped!
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Bug 2: Quick Sort Infinite Recursion (Pivot handling)
def quick_sort_buggy(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Including the pivot in the 'left' array causes infinite recursion
        # if the pivot happens to be the smallest element (or in other scenarios).
        left = [x for x in arr if x <= pivot] 
        right = [x for x in arr if x > pivot]
        
        # We also forgot to explicitly place the pivot in the middle!
        return quick_sort_buggy(left) + quick_sort_buggy(right)

if __name__ == "__main__":
    print(f"1. Merge Sort: {merge_sort_buggy([38, 27, 43, 3, 9, 82, 10])}")
    
    # WARNING: This will cause a RecursionError if not fixed!
    # print(f"2. Quick Sort: {quick_sort_buggy([10, 7, 8, 9, 1, 5])}")
