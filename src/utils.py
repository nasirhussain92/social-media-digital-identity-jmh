"""
Utility Functions

Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok

Research Reproducibility Package
"""

import pandas as pd
import numpy as np


# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

def load_dataset(path):
    """
    Load the cleaned dataset.
    """
    return pd.read_csv(path)


# -------------------------------------------------------
# Reverse Scoring
# -------------------------------------------------------

def reverse_score(df, columns, max_scale=5, min_scale=1):
    """
    Reverse-score Likert items.
    """
    for col in columns:
        df[col] = (max_scale + min_scale) - df[col]
    return df


# -------------------------------------------------------
# Composite Variables
# -------------------------------------------------------

def create_composite(df, items, variable_name):
    """
    Create a composite score using the arithmetic mean.
    """
    df[variable_name] = df[items].mean(axis=1)
    return df


# -------------------------------------------------------
# Missing Values
# -------------------------------------------------------

def missing_values(df):
    """
    Return missing values summary.
    """
    return df.isnull().sum()


# -------------------------------------------------------
# Dataset Information
# -------------------------------------------------------

def dataset_summary(df):

    print("=" * 60)
    print("Dataset Summary")
    print("=" * 60)

    print(f"Rows      : {df.shape[0]}")
    print(f"Columns   : {df.shape[1]}")
    print(f"Missing   : {df.isnull().sum().sum()}")
    print(f"Duplicate : {df.duplicated().sum()}")

    print("=" * 60)
