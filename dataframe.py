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