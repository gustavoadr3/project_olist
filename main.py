from loguru import logger
from google.cloud import storage
from scripts.validations.validation_yaml import load_yaml
from scripts.validations.validation_csv import load_csv
from scripts.validations.validation_columns import validate_columns
from scripts.bucket.import_bucket import upload_bucket


file_path_yaml_raw = r'schemas/raw'
file_path_csv = r'data'
client_json = r'/Users/gustavo/Documents/Projetos/project-olist/projectolist-483623-63de0f11da4d.json'
storage_client_gcp = storage.Client.from_service_account_json(client_json)
name_bucket = 'bucket_olist'


def main():
    yaml_files = load_yaml(file_path_yaml_raw)
    csv_files = load_csv(file_path_csv)
    validate_columns(yaml_files, csv_files)
    upload_bucket(client=storage_client_gcp, bucket_name=name_bucket, path_csv=file_path_csv)

if __name__ == '__main__':
    main()