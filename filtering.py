import pandas as pd

df = pd.read_csv('data.csv')

"""
Filtering is where you will start to find similarities with the SQL select statement. Filtering is nothing but choosing which entries are to
be displayed in our output.
"""

BMW = df[ df['make'] == 'BMW']
# print(BMW.to_string(index = False))

"""
What we are doing here is pretty simple. Just showing all the bikes which are from BMW.

The "index = False" statement here just makes it such that the output doesn't contain any index values
"""

naked_400_plus = df[ ((df['type'] == 'Naked') & (df['engine_cc'] >= 400)) | (df['type'] == 'Adventure') ]
print(naked_400_plus.to_string(index = False))

"""
Here we have used multiple conditions. But notice something.

**************************************************************************************************************************
1. In python, logical operators don't look like the ones we have used here.

Ans: The short answer is: pandas requires &, |, ~ instead of and, or, not because of how Python evaluates them.
Here's why:
Python's and/or are designed for single True/False values. When you write a and b, Python checks if a is truthy, then returns either a or b,
one single value. But df['type'] == 'Naked' doesn't return a single True/False. It returns a whole Series of booleans, like:
0     True
1    False
2     True
3    False
Python's and/or don't know how to handle a whole column of booleans — they'd throw an error like:
ValueError: The truth value of a Series is ambiguous
& and | work element-wise. They compare each row's True/False value individually across two Series, which is exactly what you need for
filtering.

**************************************************************************************************************************
2. Why do we need parenthesis () around each of our conditions?

Ans: & and | have higher operator precedence than == and >= in Python, so without the parentheses, pandas would try to evaluate something
nonsensical like df['engine_cc'] >= (400 | df['type'])
"""