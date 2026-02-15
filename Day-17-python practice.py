14/feb/2026

## Key data structure in pandas 
* Series
* Dataframe



s = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
s

df = pd.DataFrame({"name":["shivjot","pahul","nitin"], "marks":[22,33,44]})
ss = pd.DataFrame(df,index = ["a","b"],columns=[11,12])
ss

import pandas as pd 
url = "https://raw.githubusercontent.com/ShivjotChoudhary/Datasets/refs/heads/main/Titanic-Dataset.csv"
df = pd.read_csv(url)
df.head()

df.tail()

df.describe()

df.info()

aa=df["Name"]
aa.head()
# type(aa)

df[["Name" ,"Sex","Age"]][0:5]

df.iloc[0]

df.dropna()[["Name","Survived"]][0:5]

df.dropna()[0:5]

df.fillna("**")[0:5]

rn = df.rename(index={0:"A"})[:5]
rn

rn.info()

rn["Age"] = rn["Age"].astype(int)
rn=rn.fillna("**")
rn

len(df.columns)

rn["zeroes"]=[0 for i in range(len(rn))]
rn

def rc(a):
  return a*a
rn["applied function"] = rn["Pclass"].apply(rc)
rn

del rn["zeroes"]


rn.to_csv("/content/Untitled Folder/dd")

ss = pd.DataFrame([])
ss

# **Concatinating :**

df1 = pd.DataFrame({
    "name":["shivjot","nitin","gugi"],
    "marks":[99,60,40]
})
df1

df2 = pd.DataFrame({
    "name":["shivjot","nitin","gugi"],
    "roll num":[21,18,12]
})
df2

ss = pd.concat([df1,df2])
ss

df3 = pd.DataFrame({
    "name":["shivjot","nitin","dhiraj"],
    "marks":[99,60,40]
})
df3

df4 = pd.DataFrame({
    "name":["shivjot","nitin","gugi"],
    "roll num":[21,10,50]
})
df4

sd = pd.merge(df3,df4 , on = "name")
sd
