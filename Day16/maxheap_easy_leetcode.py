import heapq
import math

# ==========================================
# MAX HEAP EASY LEETCODE PROBLEMS
# ==========================================
# Note: Python's heapq is a Min-Heap by default. To simulate a Max-Heap, 
# we multiply numerical values by -1 before pushing, and multiply by -1 when popping.

# Problem 1: Last Stone Weight (LeetCode 1046)
# Difficulty: Easy
# Description: You are given an array of integers stones where stones[i] is the weight of the ith stone.
# On each turn, we choose the heaviest two stones and smash them together. 
# Return the weight of the last remaining stone. If there are no stones left, return 0.
# Approach: Create a Max-Heap out of all the stones. Pop the two heaviest, smash them,
# and push the difference back if any.

def lastStoneWeight(stones):
    # Negate values to create a Max-Heap
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Pop the two heaviest stones
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)
        
        if stone1 != stone2:
            # Push the remaining weight back as negative
            heapq.heappush(max_heap, -(stone1 - stone2))
            
    return -max_heap[0] if max_heap else 0


# Problem 2: Take Gifts From the Richest Pile (LeetCode 2558)
# Difficulty: Easy
# Description: You are given an integer array gifts denoting the number of gifts in various piles.
# Every second, you do the following:
# Choose the pile with the maximum number of gifts.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest.
# Return the number of gifts remaining after k seconds.
# Approach: Use a Max-Heap to efficiently repeatedly find and replace the maximum pile.

def pickGifts(gifts, k):
    # Create a Max-Heap by negating the gifts
    max_heap = [-gift for gift in gifts]
    heapq.heapify(max_heap)
    
    for _ in range(k):
        # Pop the pile with the maximum gifts
        max_gifts = -heapq.heappop(max_heap)
        
        # Leave behind the square root
        left_behind = math.floor(math.sqrt(max_gifts))
        
        # Push the remaining gifts back to the pile
        heapq.heappush(max_heap, -left_behind)
        
    # Return the sum of all remaining gifts (making them positive again)
    return -sum(max_heap)

if __name__ == "__main__":
    print("====================================")
    print("          MAX HEAP TESTS            ")
    print("====================================")
    
    print("\n--- Problem 1: Last Stone Weight ---")
    stones = [2, 7, 4, 1, 8, 1]
    print(f"Stones: {stones}")
    print("Result:", lastStoneWeight(stones)) # Expected: 1
    
    print("\n--- Problem 2: Take Gifts From the Richest Pile ---")
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(f"Gifts: {gifts}, k: {k}")
    print("Result:", pickGifts(gifts, k)) # Expected: 29
