def convert_to_upper(lines):
    for line in lines:
        print(line.upper())

n = int(input("Enter number of lines: "))
lines = []

for i in range(n):
    lines.append(input())

convert_to_upper(lines)