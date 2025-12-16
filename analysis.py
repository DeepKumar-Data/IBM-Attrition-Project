import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv("employee_attrition.csv")

# EDA summaries
print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("\nMissing values:", df.isnull().sum().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nAttrition:\n", df["Attrition"].value_counts())
print("\nAttrition %:\n", (df["Attrition"].value_counts(normalize=True) * 100).round(2))
print("\nOverTime vs Attrition:\n", pd.crosstab(df["OverTime"], df["Attrition"]))
print("\nDepartment vs Attrition:\n", pd.crosstab(df["Department"], df["Attrition"]))

# Centralized styling
plt.rcParams.update({
    "figure.facecolor": "#F7F9FC",
    "axes.facecolor": "#F7F9FC",
    "axes.edgecolor": "#CCCCCC",
    "font.family": "DejaVu Sans",
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
})

PRIMARY = ["#2C5F8A", "#E07B39"]
DEPT_COLORS = ["#2C5F8A", "#3A9E82", "#E07B39"]

def add_value_labels(ax, fontsize=10):
    """Add count labels on top of bars."""
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height()):,}",
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha="center", va="bottom", fontsize=fontsize, fontweight="bold")

# Chart 1: Attrition Count
fig, ax = plt.subplots(figsize=(7, 5))
df["Attrition"].value_counts().plot(kind="bar", ax=ax, color=PRIMARY, edgecolor="white", linewidth=0.8)
ax.set_title("Employee Attrition Count")
ax.set_xlabel("Attrition")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=0)
ax.spines[["top", "right"]].set_visible(False)
add_value_labels(ax)
plt.tight_layout()
plt.show()

# Chart 2: OverTime vs Attrition
fig, ax = plt.subplots(figsize=(7, 5))
pd.crosstab(df["OverTime"], df["Attrition"]).plot(kind="bar", ax=ax, color=PRIMARY, edgecolor="white", linewidth=0.8)
ax.set_title("OverTime vs Attrition")
ax.set_xlabel("OverTime")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=0)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(title="Attrition", framealpha=0.6)
add_value_labels(ax, fontsize=9)
plt.tight_layout()
plt.show()

# Chart 3: Employees by Department
fig, ax = plt.subplots(figsize=(7, 5))
df["Department"].value_counts().plot(kind="bar", ax=ax, color=DEPT_COLORS, edgecolor="white", linewidth=0.8)
ax.set_title("Employees by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
ax.tick_params(axis="x", rotation=15)
ax.spines[["top", "right"]].set_visible(False)
add_value_labels(ax)
plt.tight_layout()
plt.show()