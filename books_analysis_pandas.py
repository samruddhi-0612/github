import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Book Details:")
print(df)

author_name = input("\nEnter author name: ")
print("\nBooks by", author_name)
print(df[df['author'] == author_name])

publisher_name = input("\nEnter publisher name: ")
print("\nBooks from", publisher_name)
print(df[df['publishing_house'] == publisher_name])

print("\nCheapest Book:")
print(df[df['price'] == df['price'].min()])

print("\nCostliest Book:")
print(df[df['price'] == df['price'].max()])

print("\nBooks sorted by Year:")
print(df.sort_values(by='year'))