"""
Descriptive Statistics

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok
Research Reproducibility Package
"""

import pandas as pd


# -------------------------------------------------------
# Descriptive Statistics
# -------------------------------------------------------

def descriptive_statistics(df):

    variables = ["SMU", "DI", "EC", "SC", "SE"]

    report = pd.DataFrame({
        "Variable": variables,
        "Mean": [round(df[v].mean(), 3) for v in variables],
        "SD": [round(df[v].std(), 3) for v in variables],
        "Minimum": [round(df[v].min(), 3) for v in variables],
        "Maximum": [round(df[v].max(), 3) for v in variables],
        "Skewness": [round(df[v].skew(), 3) for v in variables],
        "Kurtosis": [round(df[v].kurtosis(), 3) for v in variables]
    })

    return report


# -------------------------------------------------------
# Export
# -------------------------------------------------------

def export_descriptive(report,
                       filename="../outputs/tables/descriptive_statistics.csv"):

    report.to_csv(filename, index=False)

    return filename
