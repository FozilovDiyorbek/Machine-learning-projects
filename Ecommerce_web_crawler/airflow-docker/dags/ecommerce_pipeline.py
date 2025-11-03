from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys, os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from crawler import run_crawler
from preprocess_data import preprocess
from feature_engineering import feature_engineering
from train_model import train_model

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ecommerce_pipeline",
    default_args=default_args,
    description="E-commerce price prediction pipeline",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    crawl_task = PythonOperator(task_id="crawl_data", python_callable=run_crawler)
    preprocess_task = PythonOperator(task_id="preprocess_data", python_callable=preprocess)
    feature_task = PythonOperator(task_id="feature_engineering", python_callable=feature_engineering)
    train_task = PythonOperator(task_id="train_model", python_callable=train_model)

    crawl_task >> preprocess_task >> feature_task >> train_task
