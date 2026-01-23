import sys
sys.path.append("/opt/airflow")

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.airflow.validation_raw import validate_raw_files


with DAG(
    dag_id="olist_pipeline",
    description="Olist end-to-end data pipeline",
    start_date=datetime(2026, 1, 23),
    schedule_interval="*/10 * * * *",
    max_active_runs = 1,
    catchup=False,
    tags=["olist", "etl"],
) as dag:

    validate_raw = PythonOperator(
        task_id="validate_raw_files",
        python_callable=validate_raw_files,
    )

    validate_raw
