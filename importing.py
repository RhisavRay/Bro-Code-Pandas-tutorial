import pandas as pd

df_csv = pd.read_csv("data.csv")

# print(df_csv.to_string())

df_json = pd.read_json("data.json")

print(df_json)
