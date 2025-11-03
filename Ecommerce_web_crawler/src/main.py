from preprocess_data import preprocess
from feature_engineering import feature_engineering
from train_model import train_model
from crawler import run_crawler

def main():
    run_crawler()
    preprocess()
    feature_engineering()
    train_model()

if __name__ == "__main__":
    main()