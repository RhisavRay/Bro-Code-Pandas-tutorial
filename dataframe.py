import pandas

"""
Dataframe - It is a tabular data structure with rows and columns (2 dimensional).
            Similar to an Excel spreadsheet.
"""

data_A = {
    "Name": ["Rhisav", "Rohan", "Raima", "Rohit"],
    "Age": [24, 23, 22, 23]
}

dataframe_A = pandas.DataFrame(data_A)
print(dataframe_A)

dataframe_B = pandas.DataFrame(data_A, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])
print(dataframe_B)

print(dataframe_B.loc["Employee 1"])
print(dataframe_B.iloc[2])

"""
Basic printing, indexing and use of loc and iloc functions remain the same for a series and a dataframe.
Similar to a series, while initializing one the keyword DataFrame is not a method. It is a constructor
"""

# Add a new column
dataframe_B["Job"] = ["Chef", "Sous Chef", "Beauty", "Idiot"]
print(dataframe_B)

"""
Now since this is kind of spreadsheet, we kinda expect it to do spreadsheet things. Like adding a new column to our data. Let us make this
step a little more easy to understand.

Take it this way. Consider that dataframe_B is like a dictionary, just like data_A from which it was created. Now how do you add a new
key-value pair in a dictionary? Similarly we do here. It would give the same result as adding the key-value pair of "Job" and the list of
jobs to data_A itself using a similar syntax.
"""

# Add a new row
# new_rows = pandas.DataFrame([{"Name": "Sandy", "Age": 35, "Job": "Scientist"},
#                             {"Name": "Crabs", "Age": 54, "Job": "Manager"}],
#                            index=["Employee 5", "Employee 6"])

# new_rows = pandas.DataFrame([{"Name": ["Sandy", "Crabs"], "Age": [35, 54], "Job": ["Scientist", "Manager"]}], index=["Employee 5", "Employee 6"])

new_rows = {
    "Name": ["Sandy", "Crabs"],
    "Age": [35, 54],
    "Job": ["Scientist", "Manager"]
}
new_rows_df = pandas.DataFrame(new_rows, index=["Employee 5", "Employee 6"])

dataframe_B = pandas.concat([dataframe_B, new_rows_df])
print(dataframe_B)

"""
Now we want to add a new row/entry to the dataframe. To do that we are creating a new dataframe with the new entry/entries, and
concatenating it to the existing dataframe.

Notice that I have tried to add these 2 new entries in 3 ways.
1. By passing a list of dictionaries, with each dictionary containing the details of one entry.
2. By passing a single dictionary with the details of both the entries at the same time, like was done when creating the dataframe.
3. Creating a dictionary separately, with the details of both the entries, and then converting it to dataframe

Out of these the 3rd one works for obvious reasons. This is how we have created a dataframe before, and it has to work now too

But by that logic the 2nd one should work too. But it turns out it doesn't. It won't throw an error, but you will see that for each new index
the entry added will contain the list of the details. In this case, it takes each dictionary as a single entry. That's why there are []
around the dictionary. It accepts a list of dictionaries.

And by that logic, does the 1st technique also works.
"""