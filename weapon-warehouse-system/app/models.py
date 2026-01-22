import pandas as pd


def cut_categorize(df):
    bins = [0, 20, 100, 300, float('inf')]
    labels = ['low', 'medium', 'high', 'extreme']
    df['risk_level'] = pd.cut(df['range_km'], bins=bins, labels=labels)
    return NaN_cleaning(df)


def NaN_cleaning(df):
    df['manufacturer'] = df['manufacturer'].fillna('Unknown')
    return df
