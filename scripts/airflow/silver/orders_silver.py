import os
import logging

from scripts.silver.validation_columns import validation_coluns
from scripts.bucket.read_bucket import read_bucket
from scripts.utils.read_yaml import read_yaml
from scripts.silver.write_silver_bigquery import write_silver_bigquery
from scripts.utils.logging_config import setup_logging


def get_base_path():
    if os.path.exists("/opt/airflow"):
        return "/opt/airflow"
    return "."


def build_orders_silver():
    setup_logging()
    logging.info("Iniciando Silver - orders")

    base_path = get_base_path()

    client_json = f"{base_path}/credentials/gcp_service_account.json"
    path_yaml = f"{base_path}/schemas/silver/orders.yaml"

    df_orders_silver = validation_coluns(
        func_read=read_bucket,
        client_json=client_json,
        func_yaml=read_yaml,
        path_yaml=path_yaml,
    )

    write_silver_bigquery(
        client_json=client_json,
        df_gcp=df_orders_silver,
        func=read_yaml,
        path_yaml=path_yaml,
    )

    logging.info("Silver - orders finalizado com sucesso")
