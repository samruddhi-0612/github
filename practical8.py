source_file = "input.txt"
destination_file = "output.txt"

with open(source_file, "r") as f:
    content = f.read()

upper_content = content.upper()

with open(destination_file, "w") as f:
    f.write(upper_content)

print("Content copied in uppercase.")

print("\nOriginal File Content:")
print(content)

print("\nUppercase File Content:")
print(upper_content)