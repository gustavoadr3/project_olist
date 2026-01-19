from google.cloud import storage
from scripts.validations.validation_yaml import load_yaml
from scripts.validations.validation_csv import load_csv
from scripts.validations.validation_columns import validate_columns
from scripts.bucket.import_bucket import upload_bucket
from scripts.bucket.read_bucket import read_bucket
from scripts.silver.validation_columns import validation_coluns
from scripts.silver.write_silver_bigquery import write_silver_bigquery
from scripts.utils.read_yaml import read_yaml


file_path_yaml_raw = r'schemas/raw'
file_path_csv = r'data'
client_json = r'/Users/gustavo/Documents/Projetos/project-olist/projectolist-483623-63de0f11da4d.json'
storage_client_gcp = storage.Client.from_service_account_json(client_json)


def main():
    yaml_files = load_yaml(file_path_yaml_raw)
    csv_files = load_csv(file_path_csv)
    validate_columns(yaml_files, csv_files)
    upload_bucket(client=storage_client_gcp, bucket_name='bucket_olist', path_csv=file_path_csv)
    df_orders_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/orders.yaml')
    df_customers_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/customers.yaml')
    df_orders_items_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/orders_items.yaml')
    df_products_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/products.yaml')
    df_sellers_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/sellers.yaml')
    df_payments_silver = validation_coluns(func_read=read_bucket, client_json=client_json, func_yaml=read_yaml, path_yaml=r'schemas/silver/orders_payments.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_payments_silver, func=read_yaml, path_yaml= r'schemas/silver/orders_payments.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_sellers_silver, func=read_yaml, path_yaml= r'schemas/silver/sellers.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_products_silver, func=read_yaml, path_yaml= r'schemas/silver/products.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_orders_items_silver, func=read_yaml, path_yaml= r'schemas/silver/orders_items.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_orders_silver, func=read_yaml, path_yaml= r'schemas/silver/orders.yaml')
    write_silver_bigquery(client_json=client_json, df_gcp=df_customers_silver, func=read_yaml, path_yaml= r'schemas/silver/customers.yaml')

if __name__ == '__main__':
    main()