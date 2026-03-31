import pandas as pd

df = pd.read_csv('data.csv')

"""
Aggregate function in pandas
1. Reduce a set of values to a single summary value.
2. Used to summarize and analyze data.
3. Often used along side the groupby() function.
"""

pd.set_option('display.float_format', '{:.2f}'.format)

"""
Before we proceed any further, we need to discuss why this line of code is written.

Without this, the output was coming in scientific notation, and not a simple float. This line is added to fix that issue. Lets break it down

pd.set_option(...)
This is a pandas utility function that lets you configure global display and behaviour settings for pandas in your current session. Think
of it like a settings menu — you're not changing your data, you're just telling pandas "from now on, display things this way."


'display.float_format'
This is the name of the specific setting you're changing. Pandas has many options you can set, and display.float_format is the one that
controls how floating point numbers are rendered when printed. The display. prefix is pandas' way of grouping all display-related settings
together.


'{:.2f}'.format
This is the most interesting part, so let's slow down here. In Python, '{:.2f}'.format is a format function — specifically, it's the .format
method of the string '{:.2f}'.

Now, {:.2f} is a format specification inside a string. Breaking it down further — the {} is a placeholder that says "put a value here", the
: introduces the formatting rules, the .2 means "2 decimal places", and the f means "treat this as a float."

So '{:.2f}'.format(1087555.5555) would produce '1087555.56'.

The key thing to notice is that you're passing just '{:.2f}'.format — without calling it with parentheses and a value. You're not calling
the function, you're passing the function itself. This is because pandas internally will call it on each float value it needs to display.
You're essentially handing pandas a tool and saying "use this whenever you need to display a float."

To tie it all together — you're telling pandas: "I want you to use this specific formatting tool every time you display a float, and that
tool should render numbers with 2 decimal places." Pandas then applies that tool consistently across all float output for the rest of the
session.
"""

# Entire dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count(numeric_only=True))

# For a single column
# print(df['engine_cc'].mean())
# print(df['engine_cc'].sum())
# print(df['engine_cc'].min())
# print(df['engine_cc'].max())
# print(df['engine_cc'].count())

"""
Why is it that even after setting the rule to not show more than 2 decimal places, I am still getting multiple decimal places in this output?


When you run df.mean(numeric_only=True), the result is a pandas Series. And pd.set_option('display.float_format', ...) specifically controls
how pandas renders a Series or DataFrame when printing. So when pandas is in charge of displaying the output, it respects your format setting
and gives you 2 decimal places.

But when you run df['engine_cc'].mean(), the result is not a pandas object at all — it's a plain Python float. A raw Python scalar value. At
that point, pandas has already done its job of computing the mean and handed the result off to Python. When you print() that, it's Python's
own print function displaying a native float, not pandas — and Python has no idea about the pd.set_option rule you set.
"""

# groupby
group = df.groupby('type')

print(group['engine_cc'].mean())
print(group['engine_cc'].sum())
print(group['engine_cc'].min())
print(group['engine_cc'].max())
print(group['engine_cc'].count())