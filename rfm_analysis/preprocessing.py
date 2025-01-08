import pandas as pd

def prepare_customer_level_data(data):
    if not all(col in data.columns for col in ['Recency', 'Frequency', 'Monetary']):
        raise ValueError("Customer-level data must include 'Recency', 'Frequency', and 'Monetary' columns.")
    return data.set_index('CustomerID')

def prepare_transactional_data(data):
    if not all(col in data.columns for col in ['CustomerID', 'TransactionDate', 'TransactionValue']):
        raise ValueError("Transactional data must include 'CustomerID', 'TransactionDate', and 'TransactionValue' columns.")
    
    data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])
    summary = data.groupby('CustomerID').agg({
        'TransactionDate': lambda x: (pd.Timestamp.now() - x.max()).days,
        'CustomerID': 'count',
        'TransactionValue': 'sum'
    }).rename(columns={
        'TransactionDate': 'Recency',
        'CustomerID': 'Frequency',
        'TransactionValue': 'Monetary'
    })
    return summary