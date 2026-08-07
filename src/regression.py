"""
Regression Analysis

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok
Research Reproducibility Package
"""

import pandas as pd
import statsmodels.api as sm


# -------------------------------------------------------
# Linear Regression
# -------------------------------------------------------

def run_regression(df, dependent, independents):
    """
    Run an Ordinary Least Squares (OLS) regression.

    Parameters
    ----------
    df : pandas.DataFrame
    dependent : str
    independents : list

    Returns
    -------
    model : statsmodels RegressionResults
    """

    X = df[independents]
    X = sm.add_constant(X)

    y = df[dependent]

    model = sm.OLS(y, X).fit()

    return model


# -------------------------------------------------------
# Regression Summary Table
# -------------------------------------------------------

def regression_table(model):

    results = pd.DataFrame({

        "Variable": model.params.index,
        "Coefficient (β)": model.params.values.round(3),
        "Std. Error": model.bse.values.round(3),
        "t": model.tvalues.values.round(3),
        "p": model.pvalues.values.round(4)

    })

    return results


# -------------------------------------------------------
# Model Statistics
# -------------------------------------------------------

def model_statistics(model):

    stats = {

        "R": round(model.rsquared ** 0.5, 3),
        "R²": round(model.rsquared, 3),
        "Adjusted R²": round(model.rsquared_adj, 3),
        "F": round(model.fvalue, 3),
        "Prob(F)": round(model.f_pvalue, 4),
        "Observations": int(model.nobs)

    }

    return pd.DataFrame([stats])


# -------------------------------------------------------
# Export
# -------------------------------------------------------

def export_regression(results,
                      filename="../outputs/tables/regression_results.csv"):

    results.to_csv(filename, index=False)

    return filename
