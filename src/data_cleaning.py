import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):

    df['bhk'] = df['size'].str.extract('(\d+)').astype(float)

    df['bath'] = df['bath'].fillna(df['bath'].median())
    df['balcony'] = df['balcony'].fillna(df['balcony'].median())
    df = df.drop(['society', 'availability', 'size'], axis=1)


    return df