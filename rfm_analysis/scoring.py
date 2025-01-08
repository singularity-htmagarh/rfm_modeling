import pandas as pd
import numpy as np

def quintile_scoring(series):
    return pd.qcut(series, q=5, labels=range(5, 0, -1))

def mean_scoring(series):
    mean = series.mean()
    return series.apply(lambda x: 5 if x > mean else 1)

def median_scoring(series):
    median = series.median()
    return series.apply(lambda x: 5 if x > median else 1)

def rfm_score(data, scoring_method='quintile', custom_scores=None):
    if scoring_method not in ['quintile', 'mean', 'median']:
        raise ValueError("scoring_method must be one of ['quintile', 'mean', 'median']")
    
    scoring_func = {
        'quintile': quintile_scoring,
        'mean': mean_scoring,
        'median': median_scoring
    }[scoring_method]

    rfm_data = data.copy()
    
    rfm_data['R_Score'] = scoring_func(rfm_data['Recency'])
    rfm_data['F_Score'] = scoring_func(rfm_data['Frequency'])
    rfm_data['M_Score'] = scoring_func(rfm_data['Monetary'])
    
    rfm_data['RFM_Score'] = (rfm_data['R_Score'] + rfm_data['F_Score'] + rfm_data['M_Score']).astype(str)
    return rfm_data