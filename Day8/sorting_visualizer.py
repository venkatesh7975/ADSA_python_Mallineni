import time

def print_array(arr, step, highlight_indices=None, action=""):
    """Helper to print the array beautifully with highlights"""
    visual = []
    for i, val in enumerate(arr):
        if highlight_indices and i in highlight_indices:
            visual.append(f"[{val}]")
        else:
            visual.append(f" {val} ")
    print(f"Step {step:>2} | {' '.join(visual)} | {action}")
    time.sleep(0.5)

def bubble_sort_visual(arr):
    print("\n" + "="*50)
    print(" BUBBLE SORT VISUALIZER ")
    print("="*50)
    n = len(arr)
    step = 0
    print_array(arr, step, action="Initial Array")
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            step += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print_array(arr, step, [j, j+1], "Swapped")
            else:
                print_array(arr, step, [j, j+1], "Compared (No Swap)")
        if not swapped:
            break
    print("Bubble Sort Complete!\n")

def selection_sort_visual(arr):
    print("\n" + "="*50)
    print(" SELECTION SORT VISUALIZER ")
    print("="*50)
    n = len(arr)
    step = 0
    print_array(arr, step, action="Initial Array")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            step += 1
            print_array(arr, step, [min_idx, j], f"Comparing min ({arr[min_idx]}) with {arr[j]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        step += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print_array(arr, step, [i, min_idx], f"Swapped minimum ({arr[i]}) into place")
    print("Selection Sort Complete!\n")

def insertion_sort_visual(arr):
    print("\n" + "="*50)
    print(" INSERTION SORT VISUALIZER ")
    print("="*50)
    n = len(arr)
    step = 0
    print_array(arr, step, action="Initial Array")
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        step += 1
        print_array(arr, step, [i], f"Selected Key: {key}")
        while j >= 0 and arr[j] > key:
            step += 1
            arr[j + 1] = arr[j]
            print_array(arr, step, [j, j+1], f"Shifted {arr[j]} right")
            j -= 1
        arr[j + 1] = key
        step += 1
        print_array(arr, step, [j+1], f"Inserted Key {key}")
    print("Insertion Sort Complete!\n")

def merge_sort_visual(arr, left=0, right=None, step=[0]):
    if right is None:
        print("\n" + "="*50)
        print(" MERGE SORT VISUALIZER ")
        print("="*50)
        right = len(arr) - 1
        print_array(arr, step[0], action="Initial Array")

    if left < right:
        mid = (left + right) // 2
        
        merge_sort_visual(arr, left, mid, step)
        merge_sort_visual(arr, mid + 1, right, step)
        
        # Merge
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(L) and j < len(R):
            step[0] += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print_array(arr, step[0], [k-1], f"Merged {arr[k-1]} into position")
            
        while i < len(L):
            step[0] += 1
            arr[k] = L[i]
            i += 1
            k += 1
            print_array(arr, step[0], [k-1], f"Merged remaining {arr[k-1]}")
            
        while j < len(R):
            step[0] += 1
            arr[k] = R[j]
            j += 1
            k += 1
            print_array(arr, step[0], [k-1], f"Merged remaining {arr[k-1]}")
            
    if left == 0 and right == len(arr) - 1:
        print("Merge Sort Complete!\n")

def quick_sort_visual(arr, low=0, high=None, step=[0]):
    if high is None:
        print("\n" + "="*50)
        print(" QUICK SORT VISUALIZER ")
        print("="*50)
        high = len(arr) - 1
        print_array(arr, step[0], action="Initial Array")

    if low < high:
        # Partition
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            step[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print_array(arr, step[0], [i, j], f"Swapped {arr[i]} and {arr[j]}")
            else:
                print_array(arr, step[0], [j, high], f"Compared {arr[j]} with pivot {pivot}")
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        step[0] += 1
        print_array(arr, step[0], [pi, high], f"Placed pivot {pivot} in correct position")

        quick_sort_visual(arr, low, pi - 1, step)
        quick_sort_visual(arr, pi + 1, high, step)
        
    if low == 0 and high == len(arr) - 1:
        print("Quick Sort Complete!\n")

if __name__ == "__main__":
    # Test arrays
    test_arr1 = [5, 2, 9, 1, 5, 6]
    test_arr2 = [5, 2, 9, 1, 5, 6]
    test_arr3 = [5, 2, 9, 1, 5, 6]
    test_arr4 = [5, 2, 9, 1, 5, 6]
    test_arr5 = [5, 2, 9, 1, 5, 6]

    bubble_sort_visual(test_arr1)
    selection_sort_visual(test_arr2)
    insertion_sort_visual(test_arr3)
    merge_sort_visual(test_arr4)
    quick_sort_visual(test_arr5)
