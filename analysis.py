"""
Employee Attrition Analysis
Comprehensive EDA and visualization suite for HR analytics.

Author: Data Analytics Team
Last updated: 2024-01-15
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import logging
from pathlib import Path
from typing import Tuple, Optional

# ── Logging Configuration ─────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ── Configuration ─────────────────────────────────────────────────────────────
CONFIG = {
    "data_path": "employee_attrition.csv",
    "output_dir": "outputs",
    "figure_size": (7, 5),
    "primary_colors": ["#2C5F8A", "#E07B39"],
    "dept_colors": ["#2C5F8A", "#3A9E82", "#E07B39"],
    "dpi": 300,
    "style": {
        "figure.facecolor": "#F7F9FC",
        "axes.facecolor": "#F7F9FC",
        "axes.edgecolor": "#CCCCCC",
        "axes.grid": False,
        "grid.color": "#E0E0E0",
        "grid.linestyle": "--",
        "font.family": "DejaVu Sans",
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    }
}

plt.rcParams.update(CONFIG["style"])

# ── Data Loading & Validation ─────────────────────────────────────────────────
def load_and_validate(filepath: str) -> pd.DataFrame:
    """
    Load CSV and perform basic validation checks.
    
    Args:
        filepath: Path to CSV file
        
    Returns:
        Validated pandas DataFrame
        
    Raises:
        FileNotFoundError: If file does not exist
        pd.errors.EmptyDataError: If CSV is empty
    """
    try:
        if not Path(filepath).exists():
            raise FileNotFoundError(f"Data file not found: {filepath}")
        
        df = pd.read_csv(filepath)
        
        if df.empty:
            raise pd.errors.EmptyDataError("CSV file is empty")
        
        logger.info(f"✓ Loaded {len(df):,} records, {len(df.columns)} columns")
        return df
    
    except Exception as e:
        logger.error(f"Failed to load data: {str(e)}")
        raise

# ── Exploratory Data Analysis ─────────────────────────────────────────────────
def print_eda_summary(df: pd.DataFrame) -> None:
    """
    Print comprehensive exploratory data analysis.
    
    Args:
        df: Input DataFrame
    """
    logger.info("="*60)
    logger.info("EXPLORATORY DATA ANALYSIS")
    logger.info("="*60)
    logger.info(f"Shape: {df.shape}")
    logger.info(f"Missing values: {df.isnull().sum().sum()}")
    logger.info(f"Duplicates: {df.duplicated().sum()}")
    logger.info(f"Attrition distribution:\n{df['Attrition'].value_counts()}")
    logger.info(f"Attrition %:\n{(df['Attrition'].value_counts(normalize=True) * 100).round(2)}")

# ── Visualization Utilities ───────────────────────────────────────────────────
def add_value_labels(ax: plt.Axes, fontsize: int = 10) -> None:
    """Add formatted count labels on top of bars."""
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height()):,}",
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha="center", va="bottom", fontsize=fontsize, 
                    fontweight="bold", color="#333333")

def format_chart(ax: plt.Axes, title: str, xlabel: str, ylabel: str, 
                 rotation: int = 0, legend_title: Optional[str] = None) -> None:
    """
    Apply standard formatting to chart axes.
    
    Args:
        ax: Matplotlib axes object
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label
        rotation: X-axis label rotation in degrees
        legend_title: Optional legend title
    """
    ax.set_title(title)
    ax.set_xlabel(xlabel, labelpad=8)
    ax.set_ylabel(ylabel, labelpad=8)
    ax.tick_params(axis="x", rotation=rotation)
    ax.spines[["top", "right"]].set_visible(False)
    
    if legend_title:
        ax.legend(title=legend_title, framealpha=0.6)

def create_bar_chart(data: pd.Series, title: str, xlabel: str, ylabel: str,
                     colors: list, rotation: int = 0, 
                     legend_title: Optional[str] = None,
                     save_path: Optional[str] = None) -> None:
    """
    Create and display a formatted bar chart.
    
    Args:
        data: Series or DataFrame to plot
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label
        colors: List of color hex codes
        rotation: X-axis label rotation
        legend_title: Optional legend title
        save_path: Optional path to save figure
    """
    fig, ax = plt.subplots(figsize=CONFIG["figure_size"], dpi=100)
    data.plot(kind="bar", ax=ax, color=colors, edgecolor="white", linewidth=0.8)
    format_chart(ax, title, xlabel, ylabel, rotation, legend_title)
    add_value_labels(ax)
    plt.tight_layout()
    
    if save_path:
        Path(CONFIG["output_dir"]).mkdir(exist_ok=True)
        filepath = Path(CONFIG["output_dir"]) / save_path
        plt.savefig(filepath, dpi=CONFIG["dpi"], bbox_inches="tight")
        logger.info(f"Saved: {filepath}")
    
    plt.show()

# ── Main Analysis ─────────────────────────────────────────────────────────────
def main() -> None:
    """Execute full analysis pipeline."""
    try:
        # Load and validate data
        df = load_and_validate(CONFIG["data_path"])
        print_eda_summary(df)
        
        # Chart 1: Attrition Count
        create_bar_chart(
            df["Attrition"].value_counts(),
            title="Employee Attrition Count",
            xlabel="Attrition",
            ylabel="Number of Employees",
            colors=CONFIG["primary_colors"],
            save_path="attrition_count.png"
        )
        
        # Chart 2: OverTime vs Attrition
        create_bar_chart(
            pd.crosstab(df["OverTime"], df["Attrition"]),
            title="OverTime vs Attrition",
            xlabel="OverTime",
            ylabel="Number of Employees",
            colors=CONFIG["primary_colors"],
            legend_title="Attrition",
            save_path="overtime_attrition.png"
        )
        
        # Chart 3: Employees by Department
        create_bar_chart(
            df["Department"].value_counts(),
            title="Employees by Department",
            xlabel="Department",
            ylabel="Number of Employees",
            colors=CONFIG["dept_colors"],
            rotation=15,
            save_path="department_employees.png"
        )
        
        logger.info("✓ Analysis complete")
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()