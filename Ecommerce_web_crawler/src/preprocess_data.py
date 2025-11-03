import pandas as pd
import glob, os

def preprocess():
    files = glob.glob("data/raw/*.csv")
    if not files:
        print("No raw data found!")
        return

    latest_file = max(files, key=os.path.getctime)
    df = pd.read_csv(latest_file)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df.dropna(inplace=True)

    os.makedirs("data/processed", exist_ok=True)
    processed_file = "data/processed/cleaned_data.csv"
    df.to_csv(processed_file, index=False)
    print(f"Cleaned data saved in {processed_file}")

if __name__ == "__main__":
    preprocess()