import heapq

# ==========================================
# MIN HEAP EASY LEETCODE PROBLEMS
# ==========================================

# Problem 1: Kth Largest Element in a Stream (LeetCode 703)
# Difficulty: Easy
# Description: Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Approach: Maintain a Min-Heap of size k. The smallest element in the heap (root) 
# will always be the kth largest element seen so far.

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        # If heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the heap is the kth largest element
        return self.min_heap[0]


# Problem 2: Find Subsequence of Length K With the Largest Sum (LeetCode 2099)
# Difficulty: Easy
# Description: You are given an integer array nums and an integer k. You want to find a 
# subsequence of nums of length k that has the largest sum.
# Approach: Use a Min-Heap of size k to find the k largest elements and their indices.
# Then sort them by their original indices to maintain the subsequence order.

def maxSubsequence(nums, k):
    min_heap = []
    
    # Store (value, index) in the min heap
    for i, num in enumerate(nums):
        heapq.heappush(min_heap, (num, i))
        # Maintain a heap size of k
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # The heap now contains the k largest elements along with their original indices.
    # We must return them in the order they appeared in the original array,
    # so we sort the remaining elements by their original index.
    min_heap.sort(key=lambda x: x[1])
    
    # Extract only the values
    return [val for val, idx in min_heap]

if __name__ == "__main__":
    print("====================================")
    print("          MIN HEAP TESTS            ")
    print("====================================")
    
    print("\n--- Problem 1: Kth Largest Element in a Stream ---")
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print("Add 3 (kth largest is 4):", kthLargest.add(3)) # returns 4
    print("Add 5 (kth largest is 5):", kthLargest.add(5)) # returns 5
    print("Add 10 (kth largest is 5):", kthLargest.add(10)) # returns 5
    print("Add 9 (kth largest is 8):", kthLargest.add(9)) # returns 8
    print("Add 4 (kth largest is 8):", kthLargest.add(4)) # returns 8
    
    print("\n--- Problem 2: Find Subsequence of Length K With the Largest Sum ---")
    nums = [2, 1, 3, 3]
    k = 2
    print(f"Nums: {nums}, k: {k}")
    print("Result:", maxSubsequence(nums, k)) # Expected: [3, 3]
