import os 
import re
from loguru import logger
from google.cloud import storage


def upload_bucket(client, bucket_name: str, path_csv: str):
    try:
        for index, name_file in enumerate(os.listdir(path_csv)):
            # Criar o client do Bucket
            bucket = client.bucket(bucket_name)

            # Tratar o CSV
            file_name = re.split(r'_|\.', name_file)
            name = f'{file_name[1]}_{file_name[2]}'
            if 'dataset' in name:
                name = name.replace('_dataset', '').replace('_', '')



            # Subir o arquivo para o Bucket
            destination_blob = f'raw/olist/{name}/{name_file}'
            blob = bucket.blob(destination_blob)
            source_file_name = f'{path_csv}/{name_file}'
            blob.upload_from_filename(source_file_name)
            logger.success(f'{destination_blob} subido com sucesso!')

    except Exception as e:
            logger.critical(f'Erro ao subir o bucket: {e}')

