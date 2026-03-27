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

"""
Let us begin by learning about selection by column.

Here we just pass the column name to the dataframe, as shown in line 11.

* NOTE: Python is case sensitive. So make sure the names used are EXACLTY matching *

If multiple columns are to be shown, pass their names as a list of values, as shown in line 13.

But if the list of columns is larger, we can also pass the range of columns, as shown in line 15.

But if you wanna use the column names, then we have to switch to .loc. So if names have to be used, they have to be used for both, column
and row names, and thus .loc has to be used. And the same for numbers as well, and .iloc has to be used.
"""

# Selection by rows
df_2 = pd.read_csv("data.csv", index_col = "model")

print(df_2.loc["Duke 390"])

print(df_2.loc[["Duke 390", "Duke 200"]])

print(df_2[45:54])

print(df_2.iloc[45:54])

print(df_2.loc["Duke 200":"RC 390"])

print(df_2.loc["Duke 200":"RC 390", "make":"model"])

print(df_2.loc["Duke 200":"RC 390":2, ["engine_cc", "horsepower", "torque_nm"]])

model_name = input("Please enter the name of the model: ")

try:
    print(df_2.loc[model_name])
except KeyError:
    print(f"{model_name} not found")


Like we did for selection by column, here too we can pass a list of values (line 39) and expect to get the details of those entries shown.

That is not the only way to show the value of multiple rows in a dataframe. We can also ask for a range of entries, from one entry to the
other by passing the entry number as shown in line 41. The reason we don't use .loc in this case is because the .loc keyword searches in the
index column. But for our case, that has been changed to the model column. So it's not needed here. Alternatively .iloc could also be used,
like in line 43.

But not always will we remember what the count of each entry is when the dataset becomes big. In that case we can make do with the value of
the index column value of each entry, as shown in line 45.

Now combining our knowledge of both kinds of selection, we have typed line 47 and 49.

Sometimes we will need to ask the user to enter a value to search for in the dataframe. We have implemented that from line 51 to 56. We also
have a try except block in place to make sure if an error is to occur due to a wrongly entered value, no error gets thrown.
"""