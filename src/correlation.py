"""
Correlation Analysis

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok
Research Reproducibility Package
"""

import pandas as pd
from scipy.stats import pearsonr


# -------------------------------------------------------
# Pearson Correlation Matrix
# -------------------------------------------------------

def correlation_matrix(df):

    variables = ["SMU", "DI", "EC", "SC", "SE"]

    corr = df[variables].corr(method="pearson")

    return corr.round(3)


# -------------------------------------------------------
# Correlation Significance Matrix
# -------------------------------------------------------

def correlation_pvalues(df):

    variables = ["SMU", "DI", "EC", "SC", "SE"]

    pvalues = pd.DataFrame(index=variables, columns=variables)

    for row in variables:
        for col in variables:

            if row == col:
                pvalues.loc[row, col] = ""

            else:
                _, p = pearsonr(df[row], df[col])

                if p < 0.001:
                    pvalues.loc[row, col] = "***"
                elif p < 0.01:
                    pvalues.loc[row, col] = "**"
                elif p < 0.05:
                    pvalues.loc[row, col] = "*"
                else:
                    pvalues.loc[row, col] = "ns"

    return pvalues


# -------------------------------------------------------
# Export
# -------------------------------------------------------

def export_correlation(corr,
                       filename="../outputs/tables/correlation_matrix.csv"):

    corr.to_csv(filename)

    return filename
