"""
Mediation Analysis

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok
Research Reproducibility Package
"""

import pandas as pd
import statsmodels.api as sm
from scipy.stats import norm


# -------------------------------------------------------
# Baron & Kenny Regression
# -------------------------------------------------------

def regression(df, y, X):

    X = sm.add_constant(df[X])
    model = sm.OLS(df[y], X).fit()

    return model


# -------------------------------------------------------
# Sobel Test
# -------------------------------------------------------

def sobel_test(a, sa, b, sb):
    """
    Performs Sobel mediation test.

    Parameters
    ----------
    a : coefficient of IV → Mediator
    sa : standard error of a
    b : coefficient of Mediator → DV
    sb : standard error of b
    """

    se = ((b**2) * (sa**2) + (a**2) * (sb**2)) ** 0.5

    z = (a * b) / se

    p = 2 * (1 - norm.cdf(abs(z)))

    return z, p


# -------------------------------------------------------
# Baron & Kenny Mediation
# -------------------------------------------------------

def mediation_analysis(df,
                       independent,
                       mediator,
                       dependent):

    # Path c
    model_c = regression(df, dependent, [independent])

    # Path a
    model_a = regression(df, mediator, [independent])

    # Paths b and c'
    model_b = regression(df,
                         dependent,
                         [independent, mediator])

    a = model_a.params[independent]
    sa = model_a.bse[independent]

    b = model_b.params[mediator]
    sb = model_b.bse[mediator]

    z, p = sobel_test(a, sa, b, sb)

    results = {

        "Path a": round(a, 3),
        "Path b": round(b, 3),
        "Path c": round(model_c.params[independent], 3),
        "Path c'": round(model_b.params[independent], 3),
        "Sobel z": round(z, 3),
        "Sobel p": round(p, 4)

    }

    return pd.DataFrame([results])


# -------------------------------------------------------
# Export
# -------------------------------------------------------

def export_mediation(results,
                     filename="../outputs/tables/mediation_results.csv"):

    results.to_csv(filename, index=False)

    return filename
