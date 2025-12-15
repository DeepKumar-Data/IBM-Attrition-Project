import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_attrition.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Attrition"].value_counts())
print(df["Attrition"].value_counts(normalize=True) * 100)
print(pd.crosstab(df["OverTime"], df["Attrition"]))
print(pd.crosstab(df["Department"], df["Attrition"]))

fig, ax = plt.subplots(figsize=(7, 5))
df["Attrition"].value_counts().plot(kind="bar", ax=ax, color=["#2C5F8A", "#E07B39"])
ax.set_title("Employee Attrition Count")
ax.set_xlabel("Attrition")
ax.set_ylabel("Number of Employees")
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))
pd.crosstab(df["OverTime"], df["Attrition"]).plot(kind="bar", ax=ax, color=["#2C5F8A", "#E07B39"])
ax.set_title("OverTime vs Attrition")
ax.set_xlabel("OverTime")
ax.set_ylabel("Number of Employees")
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))
df["Department"].value_counts().plot(kind="bar", ax=ax, color=["#2C5F8A", "#3A9E82", "#E07B39"])
ax.set_title("Employees by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
plt.show()