import pandas as pd

data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Tamil Nadu'],
    'Area': [307713, 196244, 191791, 342239, 130058],   # in sq km
    'Population': [124000000, 70000000, 68000000, 81000000, 78000000]
}

df = pd.DataFrame(data)

print("\nState Information:")
print(df)

print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()]['State'])

print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()]['State'])

df['Density'] = df['Population'] / df['Area']
print("\nWith Population Density:")
print(df)

print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()]['State'])