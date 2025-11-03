import pandas as pd

def feature_engineering():
    df = pd.read_csv("data/processed/cleaned_data.csv")

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating_num"] = df["rating"].map(rating_map)

    df["expensive"] = (df["price"] > df["price"].median()).astype(int)

    df.to_csv("data/processed/features.csv", index=False)
    print("Features engineered and saved.")

if __name__ == "__main__":
    feature_engineering()
