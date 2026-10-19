import pandas as pd


d={"name":["Ali","Ahmed"],"Age":[18,30],"Marks":[77,80]}

data=pd.DataFrame(d)
print(data)
data=pd.read_csv("iris.csv")
print(data)