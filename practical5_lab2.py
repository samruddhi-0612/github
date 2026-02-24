# Input prices
n = int(input("Enter number of items sold: "))
prices = []

for i in range(n):
    p = float(input("Enter price: "))
    prices.append(p)

t = tuple(prices)
print("Prices Tuple:", t)

# a) Total number of items sold
print("Total items sold:", len(t))

# b) Price of costliest item
max_price = max(t)
print("Costliest item price:", max_price)

# c) Print prices in ascending order
print("Prices in ascending order:", tuple(sorted(t)))

# d) Number of costliest items sold
count_max = t.count(max_price)
print("Number of costliest items sold:", count_max)