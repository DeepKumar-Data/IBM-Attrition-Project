import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_attrition.csv")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)
print("\nFirst 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nAttrition distribution:\n", df["Attrition"].value_counts())
print("\nAttrition %:\n", df["Attrition"].value_counts(normalize=True) * 100)
print("\nOverTime vs Attrition:\n", pd.crosstab(df["OverTime"], df["Attrition"]))
print("\nDepartment vs Attrition:\n", pd.crosstab(df["Department"], df["Attrition"]))

plt.rcParams.update({"figure.facecolor": "#F7F9FC", "axes.facecolor": "#F7F9FC"})
PRIMARY = ["#2C5F8A", "#E07B39"]
DEPT_COLORS = ["#2C5F8A", "#3A9E82", "#E07B39"]

fig, ax = plt.subplots(figsize=(7, 5))
df["Attrition"].value_counts().plot(kind="bar", ax=ax, color=PRIMARY, edgecolor="white")
ax.set_title("Employee Attrition Count", fontsize=14, fontweight="bold")
ax.set_xlabel("Attrition")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))
pd.crosstab(df["OverTime"], df["Attrition"]).plot(kind="bar", ax=ax, color=PRIMARY, edgecolor="white")
ax.set_title("OverTime vs Attrition", fontsize=14, fontweight="bold")
ax.set_xlabel("OverTime")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=0)
ax.legend(title="Attrition")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))
df["Department"].value_counts().plot(kind="bar", ax=ax, color=DEPT_COLORS, edgecolor="white")
ax.set_title("Employees by Department", fontsize=14, fontweight="bold")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=15)
plt.tight_layout()
plt.show()