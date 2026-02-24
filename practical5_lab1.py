n = int(input("Enter how many numbers: "))
lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

t = tuple(lst)
print("Tuple:", t)

# a) Total number of items
print("Total items:", len(t))

# b) Last item
print("Last item:", t[-1])

# c) Reverse tuple
print("Reverse tuple:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes, 5 is present")
else:
    print("No, 5 is not present")

# e) Remove first & last, sort remaining
new_t = t[1:-1]
sorted_t = tuple(sorted(new_t))
print("After removing first & last and sorting:", sorted_t)