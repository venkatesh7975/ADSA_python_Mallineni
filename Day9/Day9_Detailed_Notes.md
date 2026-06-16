# Day 9 Detailed Notes: Advanced Sorting Mechanics & Optimization

Welcome to Day 9! Today we dig deeper into the mechanics of sorting algorithms, exploring how small tweaks to Quick Sort create powerful new algorithms (like QuickSelect), and looking at how Python actually sorts your data under the hood.

---

## 0. Sorting Algorithms Comparison Chart

| Algorithm          | Best Case  | Average Case | Worst Case | Space Complexity | Stable? | In-Place? |
| ------------------ | ---------- | ------------ | ---------- | ---------------- | ------- | --------- |
| **Bubble Sort**    | O(n)       | O(n²)        | O(n²)      | O(1)             | ✅ Yes   | ✅ Yes     |
| **Selection Sort** | O(n²)      | O(n²)        | O(n²)      | O(1)             | ❌ No    | ✅ Yes     |
| **Insertion Sort** | O(n)       | O(n²)        | O(n²)      | O(1)             | ✅ Yes   | ✅ Yes     |
| **Merge Sort**     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | ✅ Yes   | ❌ No      |
| **Quick Sort**     | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | ❌ No    | ✅ Yes     |

---

## 1. QuickSelect (Finding the Kth Element)

What if you need to find the $K$th largest element in an array, but you don't need the whole array sorted? 
Sorting the array takes **O(n log n)**. We can do better! 

**QuickSelect** modifies Quick Sort. After we partition the array around a pivot, we know the exact sorted index of that pivot.
- If the pivot's index is exactly $K$, we are done!
- If $K$ is less than the pivot's index, we only recursively search the left side.
- If $K$ is greater, we only search the right side.

Because we throw away half the array at each step, the average Time Complexity drops to **O(n)**!

```python
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Kth element is in the left portion
    if k <= len(left):
        return quickselect(left, k)
    # Kth element is the pivot!
    elif k <= len(left) + len(mid):
        return pivot
    # Kth element is in the right portion
    else:
        # We must adjust K because we chopped off the left and mid parts
        return quickselect(right, k - len(left) - len(mid))
```

---

## 2. Quick Sort Partition Schemes

There are two famous ways to partition an array in-place for Quick Sort.

### Lomuto Partition Scheme
- Chooses the **last element** as the pivot.
- Maintains an index `i` of smaller elements, and iterates `j` across the array.
- **Pros:** Easier to implement and understand.
- **Cons:** Performs more swaps than Hoare.

### Hoare Partition Scheme
- Uses **two pointers** (one starting at the left, one at the right).
- They move towards each other. The left pointer stops when it finds an element larger than the pivot. The right pointer stops when it finds an element smaller. They swap, and continue.
- **Pros:** Does 3x fewer swaps on average compared to Lomuto. Highly efficient.

---

## 3. Counting Inversions using Merge Sort

An "inversion" is a pair of elements `(arr[i], arr[j])` such that `i < j` but `arr[i] > arr[j]`. It measures how "unsorted" an array is.
- A sorted array has 0 inversions.
- A reversed array has $\frac{n(n-1)}{2}$ inversions.

We can count inversions in **O(n log n)** time by modifying Merge Sort. 
During the merge step, if we pull an element from the `right` array before the `left` array, it means that element is smaller than *all remaining elements* in the `left` array! We add the remaining length of the `left` array to our inversion count.

---

## 4. Real-World Sorting: Timsort

When you call `arr.sort()` in Python, or `Arrays.sort()` in Java, they do not use plain Quick Sort or Merge Sort. They use **Timsort**.

Timsort is a highly optimized hybrid algorithm created by Tim Peters in 2002 for Python.
1. It scans the array looking for existing "runs" (chunks of data that are already sorted).
2. It uses **Insertion Sort** to build small runs (because Insertion Sort is incredibly fast on small, nearly-sorted arrays).
3. It uses **Merge Sort** to combine these runs together.

By leveraging existing order in the data, Timsort frequently achieves **O(n)** time complexity on real-world datasets!
