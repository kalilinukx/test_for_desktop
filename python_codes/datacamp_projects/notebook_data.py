
"""
Jupyter notebooks ♡ data
We've seen that notebooks can display basic objects such as numbers and strings. But notebooks also support the objects used in data science, which makes them great for interactive data analysis!

For example, below we create a pandas DataFrame by reading in a csv-file with the average global temperature for the years 1850 to 2016. If we look at the head of this DataFrame the notebook will render it as a nice-looking table.
"""
# Importing the pandas module
import pandas as pd
# Reading in the global temperature data
global_temp = pd.read_csv('global_temperature.csv')
print(global_temp)
​
# Take a look at the first datapoints
# ... YOUR CODE FOR TASK 3 ...
