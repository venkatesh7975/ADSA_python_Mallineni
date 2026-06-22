import heapq
from collections import Counter

# ==========================================
# IMPORTANT HEAP LEETCODE PROBLEMS
# ==========================================

# 1. Kth Largest Element in an Array (LeetCode 215) - Medium
# Approach: Use a Min-Heap of size k.
def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# 2. Top K Frequent Elements (LeetCode 347) - Medium
# Approach: Count frequencies, then use a Min-Heap of size k based on frequencies.
def topKFrequent(nums, k):
    count = Counter(nums)
    min_heap = []
    for num, freq in count.items():
        # Store as tuple (frequency, element)
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq, num in min_heap]

# 3. Last Stone Weight (LeetCode 1046) - Easy
# Approach: Use a Max-Heap to constantly smash the two heaviest stones.
def lastStoneWeight(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        s1 = -heapq.heappop(max_heap)
        s2 = -heapq.heappop(max_heap)
        if s1 != s2:
            heapq.heappush(max_heap, -(s1 - s2))
    return -max_heap[0] if max_heap else 0

# 4. Merge K Sorted Lists (LeetCode 23) - Hard
# Approach: Use a Min-Heap. Push the head of each linked list. 
# Pop the smallest, attach to result, and push its next node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # To handle ties in values when pushing to heap, we use the list index 'i'
    # since ListNode doesn't support direct comparison in python3.
    min_heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
            
    dummy = ListNode(0)
    curr = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
            
    return dummy.next

# Helper methods to build and print linked lists for testing
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return " -> ".join(res)

# 5. Find Median from Data Stream (LeetCode 295) - Hard
# Approach: Use two heaps. A Max-Heap for the smaller half, Min-Heap for the larger half.
class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half (invert values)
        self.small = []
        # min_heap stores the larger half
        self.large = []

    def addNum(self, num):
        # Push to max heap first
        heapq.heappush(self.small, -num)
        
        # Make sure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes: small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    print("=========================================")
    print("    IMPORTANT HEAP PROBLEMS TESTS        ")
    print("=========================================")
    
    print("\n1. Kth Largest Element:")
    print("   Input: [3,2,1,5,6,4], k=2")
    print("   Result:", findKthLargest([3,2,1,5,6,4], 2)) # Expected 5
    
    print("\n2. Top K Frequent Elements:")
    print("   Input: [1,1,1,2,2,3], k=2")
    print("   Result:", topKFrequent([1,1,1,2,2,3], 2)) # Expected [1, 2] or [2, 1]
    
    print("\n3. Last Stone Weight:")
    print("   Input: [2,7,4,1,8,1]")
    print("   Result:", lastStoneWeight([2,7,4,1,8,1])) # Expected 1
    
    print("\n4. Merge K Sorted Lists:")
    l1 = build_linked_list([1,4,5])
    l2 = build_linked_list([1,3,4])
    l3 = build_linked_list([2,6])
    merged = mergeKLists([l1, l2, l3])
    print("   Input: [1->4->5], [1->3->4], [2->6]")
    print("   Result:", print_linked_list(merged)) # Expected 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    
    print("\n5. Find Median from Data Stream:")
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print("   After adding [1, 2], Median:", mf.findMedian()) # Expected 1.5
    mf.addNum(3)
    print("   After adding [3], Median:", mf.findMedian()) # Expected 2
