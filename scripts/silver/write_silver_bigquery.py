from os import path
import pandas_gbq
from pandas import DataFrame
from typing import Callable
from loguru import logger 
from google.oauth2 import service_account

def write_silver_bigquery(client_json: str, df_gcp: DataFrame, func: Callable, path_yaml: str):
    try:

        configs = func(path=path_yaml)     
        table = configs["table"]
        name_table = table["dataset"]
        table_id = f"olist_silver.{name_table}"

        credentials =  service_account.Credentials.from_service_account_file(
                        client_json,
                        scopes=["https://www.googleapis.com/auth/cloud-platform"]
                        )

        pandas_gbq.context.credentials = credentials
        pandas_gbq.context.project = "projectolist-483623"

        pandas_gbq.to_gbq(
                            dataframe=df_gcp,
                            destination_table=table_id,
                            project_id="projectolist-483623",
                            if_exists="replace",
                            progress_bar=True
                        )
        logger.success(f"{table_id} subida no Bigquery")
    
    except Exception as e:
        logger.error(f"Erro ao subir a tabela {table_id}: {e}")