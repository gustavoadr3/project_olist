import pandas as pd 
import yaml
import os 

def load_yaml(file_path: str) -> dict:
    list_yaml = []
    for i in os.listdir(file_path):
        with open(os.path.join(file_path, i), 'r', encoding='utf-8') as file:
            list_yaml.append(yaml.safe_load(file))
    return list_yaml


