"""
Reliability Analysis

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok
Research Reproducibility Package
"""

import pandas as pd
import pingouin as pg


# -------------------------------------------------------
# Cronbach's Alpha
# -------------------------------------------------------

def cronbach_alpha(df, items):
    """
    Compute Cronbach's Alpha for a list of questionnaire items.
    """
    alpha, _ = pg.cronbach_alpha(data=df[items])
    return round(alpha, 3)


# -------------------------------------------------------
# Reliability Summary
# -------------------------------------------------------

def reliability_report(df):

    constructs = {

        "Social Media Usage": ["SMU1","SMU2","SMU3","SMU4","SMU5"],

        "Digital Identity": ["DI1","DI2","DI3","DI4","DI5"],

        "Emotional Coping": ["EC1","EC2","EC3","EC4"],

        "Social Comparison": ["SC1","SC2","SC3","SC4","SC5"],

        "Self-Esteem": ["SE1","SE2","SE3","SE4","SE5",
                        "SE6","SE7","SE8","SE9","SE10"]
    }

    results = []

    for construct, items in constructs.items():

        alpha = cronbach_alpha(df, items)

        results.append({
            "Construct": construct,
            "Items": len(items),
            "Cronbach Alpha": alpha
        })

    report = pd.DataFrame(results)

    return report
