import pandas as pd
df = pd.read_csv("unclean_data 1.csv",encoding = "ANSI")
print(df.columns)
df.columns = df.columns.str.lower()
print(df.columns)
df = df.rename(columns = {"duration":"TIME"})#renames a column duration to time

print(df.isnull())#display all columns
pd.set_option("display.max_columns", None)#all all
print(df.isnull().any())#if columns is missing a value
print(df.isnull().sum())#how many are missing in each
print(df.isnull().sum().sum())#the total number missing
print(df.head(5))#missing values - NaN
df = df.fillna(0)#fill the missing values with 0
print(df.head(5))
new_values = {"TIME":100,"facenumber_in_poster":-999}
df = df.fillna(value = new_values)#replace NaN in 2 columns with different values
mean_t = df["TIME"].mean()
df["TIME"] = df.TIME.fillna(mean_t)#replace all NaN with mean value in that column
print(df.head(5))
"""
.median()
.std() - standard deviation
.min()
.max()
.mode()
"""
df.dropna(inplace = True)#will drop all the rows in the table that have missing values :}
#inplace = True can be used instead of
df = df.dropna()
