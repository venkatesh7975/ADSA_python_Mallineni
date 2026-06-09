# Day 5 Practice Problems

# Problem 1: Sum all numbers in a list
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Problem 2: Product of all numbers in a list
def product_list(nums):
    if not nums:
        return 0
    product = 1
    for num in nums:
        product *= num
    return product

# Problem 3: Frequencies count of values
def count_frequencies(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Problem 4: Sum of squares
def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num * num
    return total

# Problem 5: Printing squares
def print_squares(nums):
    squares = [num * num for num in nums]
    print("Squares:", squares)
    return squares

# Problem 6: Printing all combination pairs in a given list
def print_combination_pairs(nums):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((nums[i], nums[j]))
    return pairs

if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    print("Sum:", sum_list(test_list))
    print("Product:", product_list(test_list))
    print("Frequencies:", count_frequencies([1, 2, 2, 3, 1, 4]))
    print("Sum of Squares:", sum_of_squares(test_list))
    print_squares(test_list)
    print("Combination Pairs:", print_combination_pairs(test_list))
