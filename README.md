# IBM HR Attrition Analysis

## Description
A data-driven exploratory data analysis (EDA) project focused on analyzing employee attrition rates within IBM. Using the provided dataset, the project investigates key relationships and potential drivers behind employee turnover, providing visual insights into how factors like overtime and departmental distribution influence staff retention.

## Features
- **Data Quality Assessment:** Initial inspection of dataset shape, structure, missing values, and duplicate records.
- **Attrition Profiling:** Calculation of overall attrition counts and percentages across the workforce.
- **Cross-Tabulation Analysis:** Examining relationships between employee attrition and critical variables like `OverTime` and `Department`.
- **Data Visualization:** Producing clean, formatted bar charts with direct value annotations using `matplotlib` to highlight:
    - Overall attrition volume
    - The impact of overtime on attrition rates
    - The distribution of employees across business departments

## Tech Stack
- **Language:** Python
- **Libraries:** `pandas`, `matplotlib`
- **Environment:** Jupyter Notebook (`.ipynb`) and standard Python environments.

## Setup Steps
1. Ensure the dataset `employee_attrition.csv` is located in the same directory as the scripts.
2. Install necessary libraries (e.g., `pip install pandas matplotlib`).
3. Run `python analysis.py` to print console statistics and display the sequential matplotlib bar charts.


## Folder Notes
- **`employee_attrition.csv`**: The primary dataset used for this project.
- **`analysis.py`**: A python script that executes data summaries, cross-tabulations, and plots the visuals.
- **`outputs/`**: Saved snapshots of the generated visual charts.
- **Documentation (`.pdf`, `.pptx`)**: Detailed project report and presentation slides providing analytical conclusions.
