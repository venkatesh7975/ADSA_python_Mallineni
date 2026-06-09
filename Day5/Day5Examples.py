# Day 5 Examples: Lists and Strings

# 1. String Slicing and Indexing
text = "Hello Python"
print("First char:", text[0])
print("Last char:", text[-1])
print("Slice [0:5]:", text[0:5])
print("Reverse:", text[::-1])

# 2. List Slicing All Possible Cases
nums = [1, 2, 3, 4, 5, 6, 7]
print("List:", nums)
print("Slice [1:4]:", nums[1:4])
print("Slice [:3] (first 3):", nums[:3])
print("Slice [3:] (from index 3):", nums[3:])
print("Slice [::2] (even indices):", nums[::2])
print("Slice [::-1] (reversed):", nums[::-1])

# 3. List Methods
my_list = [10, 20, 30]
my_list.append(40)
print("After append(40):", my_list)

my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

my_list.remove(20)
print("After remove(20):", my_list)

popped = my_list.pop()
print("Popped item:", popped, "Remaining:", my_list)

my_list.extend([50, 60, 30])
print("After extend:", my_list)
print("Count of 30:", my_list.count(30))

# 4. Reading Different Types of Inputs (Commented out so it doesn't block execution)
# n = int(input("Enter a number: "))
# arr = list(map(int, input("Enter space-separated numbers: ").split()))
# print("You entered list:", arr)
