import pandas as pd 
import os 

def load_csv(file_path: str) -> dict:
    list_csv = {}
    for i in os.listdir(file_path):
        if i.endswith('.csv'):
            table_name = i.replace('.csv', '',)
            table_name = table_name.replace('olist_', '')
            table_name = table_name.replace('_dataset', '',)
            df = pd.read_csv(os.path.join(file_path, i))
            columns = df.columns.to_list()
            list_csv[table_name] = columns
    return list_csv

