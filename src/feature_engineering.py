def convert_sqft(x):
    try:
        if '-' in str(x):
            a, b = x.split('-')
            return (float(a) + float(b)) / 2
        return float(x)
    except:
        return None

def feature_engineering(df):
    df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
    df = df.dropna()

    df = df[df['total_sqft'] / df['bhk'] >= 300]

    return df