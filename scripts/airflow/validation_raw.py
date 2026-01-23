import os
import logging
from loguru import logger
from scripts.utils.logging_config import setup_logging
from scripts.validations.validation_yaml import load_yaml
from scripts.validations.validation_csv import load_csv
from scripts.validations.validation_columns import validate_columns


def get_base_path():
    if os.path.exists("/opt/airflow"):
        return "/opt/airflow"
    return "."


def validate_raw_files():

    setup_logging()
    logger.info("Iniciando a validacao RAW")
    base_path = get_base_path()

    file_path_yaml_raw = f"{base_path}/schemas/raw"
    file_path_csv = f"{base_path}/data"

    yaml_files = load_yaml(file_path_yaml_raw)
    csv_files = load_csv(file_path_csv)
    validate_columns(yaml_files, csv_files)
    logger.success("Validacao concluida com sucesso")