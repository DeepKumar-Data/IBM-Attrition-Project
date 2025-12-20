import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Configuration ─────────────────────────────────────────────────────────────
CONFIG = {
    "data_path": "employee_attrition.csv",
    "figure_size": (7, 5),
    "primary_colors": ["#2C5F8A", "#E07B39"],
    "dept_colors": ["#2C5F8A", "#3A9E82", "#E07B39"],
    "style": {
        "figure.facecolor": "#F7F9FC",
        "axes.facecolor": "#F7F9FC",
        "axes.edgecolor": "#CCCCCC",
        "font.family": "DejaVu Sans",
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
    }
}

plt.rcParams.update(CONFIG["style"])

# ── Data Loading ──────────────────────────────────────────────────────────────
def load_and_validate(filepath):
    """Load CSV and perform basic validation."""
    df = pd.read_csv(filepath)
    print(f"✓ Loaded {len(df)} records, {len(df.columns)} columns")
    return df

# ── Exploratory Analysis ──────────────────────────────────────────────────────
def print_eda_summary(df):
    """Print comprehensive EDA."""
    print("\n" + "="*60)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*60)
    print(f"\nShape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print(f"\nAttrition distribution:\n{df['Attrition'].value_counts()}")
    print(f"\nAttrition %:\n{(df['Attrition'].value_counts(normalize=True) * 100).round(2)}")
    print(f"\nOverTime vs Attrition:\n{pd.crosstab(df['OverTime'], df['Attrition'])}")
    print(f"\nDepartment vs Attrition:\n{pd.crosstab(df['Department'], df['Attrition'])}")

# ── Visualization Utilities ───────────────────────────────────────────────────
def add_value_labels(ax, fontsize=10):
    """Add count labels on top of bars."""
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height()):,}",
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha="center", va="bottom", fontsize=fontsize, fontweight="bold", color="#333333")

def format_chart(ax, title, xlabel, ylabel, rotation=0, legend_title=None):
    """Apply standard formatting to chart."""
    ax.set_title(title)
    ax.set_xlabel(xlabel, labelpad=8)
    ax.set_ylabel(ylabel, labelpad=8)
    ax.tick_params(axis="x", rotation=rotation)
    ax.spines[["top", "right"]].set_visible(False)
    if legend_title:
        ax.legend(title=legend_title, framealpha=0.6)

def create_bar_chart(data, title, xlabel, ylabel, colors, rotation=0, legend_title=None):
    """Create and display a bar chart."""
    fig, ax = plt.subplots(figsize=CONFIG["figure_size"])
    data.plot(kind="bar", ax=ax, color=colors, edgecolor="white", linewidth=0.8)
    format_chart(ax, title, xlabel, ylabel, rotation, legend_title)
    add_value_labels(ax)
    plt.tight_layout()
    plt.show()

# ── Main Analysis ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df = load_and_validate(CONFIG["data_path"])
    print_eda_summary(df)
    
    # Chart 1: Attrition Count
    create_bar_chart(
        df["Attrition"].value_counts(),
        title="Employee Attrition Count",
        xlabel="Attrition",
        ylabel="Number of Employees",
        colors=CONFIG["primary_colors"]
    )
    
    # Chart 2: OverTime vs Attrition
    create_bar_chart(
        pd.crosstab(df["OverTime"], df["Attrition"]),
        title="OverTime vs Attrition",
        xlabel="OverTime",
        ylabel="Number of Employees",
        colors=CONFIG["primary_colors"],
        legend_title="Attrition"
    )
    
    # Chart 3: Employees by Department
    create_bar_chart(
        df["Department"].value_counts(),
        title="Employees by Department",
        xlabel="Department",
        ylabel="Number of Employees",
        colors=CONFIG["dept_colors"],
        rotation=15
    )