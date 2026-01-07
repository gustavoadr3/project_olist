from loguru import logger
from scripts.validations.validation_yaml import load_yaml
from scripts.validations.validation_csv import load_csv
from scripts.validations.validation_columns import validate_columns

file_path_yaml = 'schemas'
file_path_csv = r'data\raw/olist'

def main():
    yaml_files = load_yaml('schemas')
    csv_files = load_csv('data')
    validate_columns(yaml_files, csv_files)

if __name__ == '__main__':
    main()