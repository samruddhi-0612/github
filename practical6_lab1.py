s = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
uppercase = 0

for ch in s:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == " ":
        spaces += 1

    if ch.isupper():
        uppercase += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)
print("Number of uppercase letters:", uppercase)