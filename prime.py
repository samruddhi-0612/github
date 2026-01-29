while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > 1 and end > start:
        break
    else:
        print("Please enter valid numbers")

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
