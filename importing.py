import pandas as pd

df_csv = pd.read_csv("data.csv")

# print(df_csv.to_string())

df_json = pd.read_json("data.json")

print(df_json)

"""
There is nothing much in terms of importing in pandas.

Just one thing. If the dataset has several rows, only first 5 ad last 5 are shown. Also if too many columns, then only first 2 and last 2
are shown. The actual size gets mentioned below.

If you do want to see the full expanded dataset, just use ".to_string()", like shown in the commented out print statement
"""