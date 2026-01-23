import os
import logging
from google.cloud import storage

from scripts.bucket.import_bucket import upload_bucket
from scripts.utils.logging_config import setup_logging


def get_base_path():
    if os.path.exists("/opt/airflow"):
        return "/opt/airflow"
    return "."


def upload_raw_to_gcs():
    setup_logging()
    logging.info("Iniciando upload dos arquivos RAW para o GCS")

    base_path = get_base_path()

    data_path = f"{base_path}/data"
    credentials_path = f"{base_path}/credentials/gcp_service_account.json"
    bucket_name = "bucket_olist"

    client = storage.Client.from_service_account_json(credentials_path)

    upload_bucket(
        client=client,
        bucket_name=bucket_name,
        path_csv=data_path,
    )

    logging.info("Upload RAW para o GCS finalizado com sucesso")
