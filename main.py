import pandas

# print(pandas.__version__)
# The above statement can be used to check the version of pandas installed in our system\

"""
Series: A pandas 1-dimensional labeled array that can store any data type.
        You can think of it as a single column in a spreadsheet.
"""

data = [100, 101, 102, 103]
series_A = pandas.Series(data)
print(series_A)

"""
In the above lines of code, a list of integers is converted to a Series using pandas.
Upon printing the series, we see the following result:

0    100
1    101
2    102
3    103
dtype: int64

The first column is for index with a label(remember. Will come handy later), and the next column is where our data got stored.
After the data gets printed, the meta-data of the series is also printed below. This changes based on the data type being stored in the
series.
For example, for all integer values, it shows
dtype: int64
For any float value in the mix, it shows
dtype: float64
For any character value in the mix, it shows
dtype: object
For all boolean values, it shows
dtype: bool

NOTE: Series() is not a method. It is a constructor
"""

series_B = pandas.Series(data, index=["a", "b", "c", "d"])
print(series_B)

"""
Like I said for the previous example, in column 1 we could see the index of each value with a label. The default behaviour of this label
is to start from 0 and increment by 1 for each element in the series.
Now if you want this to look different, you can add a custom label. A custom label can be a list, tuple, dictionary, NumPy array or
another series.
For the second example we have used a list as the new template
"""

value_1 = series_A.loc[2]
print(value_1)
value_2 = series_B.loc["b"]
print(value_2)

"""
To access these values, we have to use the ".loc" keyword and then within the [] add the label against the data we want. This value will
be in accordance to the label used for that particular series
"""

value_3 = series_B.iloc[0]
print(value_3)
