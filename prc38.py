import pandas as pd

# Creating DataFrames

data_dict = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [18, 20, 19],
    "Marks": [77, 85, 90]
}

data_list = [
    ["Ali", 18, 77],
    ["Ahmed", 20, 85],
    ["Sara", 19, 90]
]

df1 = pd.DataFrame(data_dict)
df2 = pd.DataFrame(data_list, columns=["Name", "Age", "Marks"])

# Reading CSV file

dat = pd.read_csv("iris.csv")

print(dat.head())                 # First 5 rows
print(dat.ndim)                   # Number of dimensions
print(dat.dtypes)                 # Data types
print(dat.size)                   # Total number of values number of rows * number of columns
print(dat.columns)                # Column names
print(dat.shape)                  # Rows and columns(r,c)
print(dat.shape[0])               # Number of rows
print(dat.shape[1])               # Number of columns
dat.info()                        # DataFrame information
print(dat.describe())             # Statistical summary

# Statistical functions

print(dat.mean(numeric_only=True))
print(dat.median(numeric_only=True))
print(dat.mode())
print(dat.max(numeric_only=True))
print(dat.min(numeric_only=True))
print(dat.isnull().sum())          # Missing values

# Dropping rows and columns

# dat.drop("Id", axis=1, inplace=True)  # Remove column
# dat.drop(1, axis=0, inplace=True)      # Remove row

# Selecting and filtering with loc

print(dat.loc[12:26, "SepalWidthCm":"Species"])
print(dat.loc[dat["Species"] == "Iris-setosa"])

# Grouping by one column: 3 species groups

new = dat.groupby("Species")
print(new["SepalLengthCm"].mean())
print(new["Id"].mean())

# Grouping by two columns: unique combinations

n = dat.groupby(["Species", "PetalWidthCm"])
print(n["SepalWidthCm"].mean())
print(n["SepalWidthCm"].max())
print(n["SepalWidthCm"].min())
print(n["SepalWidthCm"].median())
print(n.mean(numeric_only=True))
print(n["SepalWidthCm"].agg(["mean", "median", "max"]))

# Removing a column and storing it separately

target = dat.pop("Species")
print(target)

# Creating three DataFrames

data1 = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Zara"],
    "Age": [22, 25, 28, 24, 30],
    "Title": ["Manager", "Developer", "Designer", "Developer", "Manager"]
}

data2 = {
    "Name": ["Hamza", "Ayesha", "Bilal", "Hira", "Saad"],
    "Age": [18, 19, 20, 18, 21],
    "Title": ["Student", "Student", "Class Rep", "Student", "Class Rep"]
}

data3 = {
    "Name": ["Usman", "Ali", "Fatima", "Ahmed", "Hassan"],
    "Age": [35, 29, 32, 35, 27],
    "Title": ["Director", "Analyst", "Manager", "Director", "Analyst"]
}

a = pd.DataFrame(data1)
b = pd.DataFrame(data2)
c = pd.DataFrame(data3)

# Concatenating DataFrames vertically

print(pd.concat([a, b], ignore_index=True))

# Merging DataFrames

print(pd.merge(a, b, how="inner"))            # Matching all shared columns

print(pd.merge(a, c, on="Name", how="inner")) # Only matching names
print(pd.merge(a, c, on="Name", how="outer")) # All names from both
print(pd.merge(a, c, on="Name", how="left"))  # All rows from a
print(pd.merge(a, c, on="Name", how="right")) # All rows from c