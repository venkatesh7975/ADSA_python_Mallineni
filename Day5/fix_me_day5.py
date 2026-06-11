# Debugging Practice: Day 5
# Topics: List Basics, Indexing, Slicing, Frequency Count, Pairs
# There are 4 intentional bugs in this script. Find and fix them!

print("--- Day 5 Debugging Challenge ---")

# Bug 1: Reverse List Slicing
def reverse_list(lst):
    # We want to reverse the list entirely
    # The step -1 is correct, but the slice is slightly off
    return lst[0:-1:-1]

# Bug 2: Frequency Count Logic
def count_freq(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] = 1 # We should be incrementing, not setting to 1!
        else:
            freq[num] = 1
    return freq

# Bug 3: Find all pairs
def find_pairs(lst):
    # We want to print all unique pairs without pairing an element with itself
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            # This logic pairs elements with themselves (i == j)
            # and produces duplicate pairs (e.g. (1,2) and (2,1))
            pairs.append((lst[i], lst[j]))
    return pairs

# Bug 4: Sum of Squares
def sum_of_squares(lst):
    total = 0
    for num in lst:
        # We want to add the square of the number to total
        total = total + num ^ 2 # ^ is XOR in Python, not exponent!
    return total

if __name__ == "__main__":
    print(f"1. Reversed: {reverse_list([1, 2, 3, 4, 5])}")
    print(f"2. Frequencies: {count_freq([1, 2, 2, 3, 1, 1])}")
    print(f"3. Pairs: {find_pairs([1, 2, 3])}")
    print(f"4. Sum of Squares: {sum_of_squares([2, 3, 4])}")
