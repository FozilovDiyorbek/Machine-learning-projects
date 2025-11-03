import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    df = pd.read_csv("data/processed/features.csv")

    X = df[["rating_num", "expensive"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model trained. R2 score: {score:.3f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/price_predictor.pkl")

if __name__ == "__main__":
    train_model()