import sys
sys.path.append("/opt/airflow")
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from scripts.airflow.validation_raw import validate_raw_files
from scripts.airflow.upload_raw_gcs import upload_raw_to_gcs
from scripts.airflow.silver.orders_silver import build_orders_silver
from scripts.airflow.silver.customers_silver import build_customers_silver
from scripts.airflow.silver.orders_items_silver import build_orders_items_silver
from scripts.airflow.silver.products_silver import build_products_silver
from scripts.airflow.silver.sellers_silver import build_sellers_silver
from scripts.airflow.silver.payments_silver import build_orders_payments_silver

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

    upload_gcs = PythonOperator(
        task_id = "upload_raw_to_gcs",
        python_callable=upload_raw_to_gcs
    )

    orders_silver = PythonOperator(
        task_id="orders_silver",
        python_callable=build_orders_silver
    )

    customers_silver = PythonOperator(
        task_id="customers_silver",
        python_callable=build_customers_silver
    )

    ordems_items_silver = PythonOperator(
        task_id="orders_items_silver",
        python_callable=build_orders_items_silver
    )

    producst_silver = PythonOperator(
        task_id="products_silver",
        python_callable=build_products_silver
    )

    sellers_silver = PythonOperator(
        task_id="sellers_silver",
        python_callable=build_sellers_silver
    )

    orders_payments_silver = PythonOperator(
        task_id="orders_payments_silver",
        python_callable=build_orders_payments_silver
    )

    dbt_run_staging = BashOperator(
        task_id="dbt_run_staging",
        bash_command="""
        cd /opt/airflow/dbt &&
        dbt run --select staging
        """,
    )

    dbt_run_gold = BashOperator(
        task_id="dbt_run_gold",
        bash_command="""
        cd /opt/airflow/dbt &&
        dbt run --select gold
        """,
    )

    dbt_run_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /opt/airflow/dbt && 
        dbt test
        """,
    )

    validate_raw >> upload_gcs >>   [orders_silver, 
                                    customers_silver, 
                                    ordems_items_silver,
                                    producst_silver,
                                    sellers_silver,
                                    orders_payments_silver] >> dbt_run_staging >> dbt_run_gold >> dbt_run_test
