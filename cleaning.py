import pandas as pd

df = pd.read_csv('data.csv')

"""
Data cleaning is the process of fixing/removing incomplete, incorrect or irrelevant data
"""

# Drop irrelevant column(s)
# df = df.drop(columns=['make', 'model'])
# print(df)


# Handle missing data
# df = df.dropna(subset=['make'])
# df = df.fillna({'make': 'No maker'})


# Fix inconsistent values
# df['type'] = df['type'].replace({'Naked': 'N',
#                                  'Sport': 'S',
#                                  'Touring': 'T',
#                                  'Adventure': 'A',
#                                  'Cruiser': 'C',
#                                  'Dirt': 'D'})


# Standardize text
# df['make'] = df['make'].str.lower()


# Fix data types
# df['engine_cc'] = df['engine_cc'].astype(bool)


# Remove duplicate values
# df = df.drop_duplicates()

print(df.to_string(index=False))