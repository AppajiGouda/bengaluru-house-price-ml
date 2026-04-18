from src.data_cleaning import load_data, clean_data
from src.feature_engineering import feature_engineering
from src.model_training import train_models
from src.evaluate import evaluate

from sklearn.model_selection import train_test_split
import pandas as pd

df = load_data("data/Bengaluru_House_Data.csv")
df = clean_data(df)
df = feature_engineering(df)

df = pd.get_dummies(df, drop_first=True)
df = df.astype(float)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y)

models = train_models(X_train, y_train)

for name, model in models.items():
    print(name, evaluate(model, X_test, y_test))