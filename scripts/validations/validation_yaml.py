import pandas as pd 
import yaml
import os 

def load_yaml(file_path: str) -> dict:
    dict_final = {}
    for i in os.listdir(file_path):
        with open(os.path.join(file_path, i), 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)
            dict_final[dados['table']] = dados['columns']
    return dict_final


