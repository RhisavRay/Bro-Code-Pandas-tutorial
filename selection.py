import pandas as pd

"""
Selection in pandas is nothing but choosing what data to show in our output statement, be it based on which column to show or which row to
show.
"""

df_1 = pd.read_csv("data.csv")

# Selection by column
print(df_1["model"])

print(df_1[["make", "model", "engine_cc"]])

print(df_1.iloc[:, 3:5])

print(df_1.loc[:, "make":"engine_cc"])

