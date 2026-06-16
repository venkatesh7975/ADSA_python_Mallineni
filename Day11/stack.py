stack=[5, 3, 8, 2, 9]
l=len(stack)
t=82
for i in range(l):
    if stack.pop() == t:
        print("Found")
        break