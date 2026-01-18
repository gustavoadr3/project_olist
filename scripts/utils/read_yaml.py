import yaml
from typing import Dict

def read_yaml(path: str) -> Dict:
    with open (path, 'r') as file:
        configs = yaml.safe_load(file)
        return configs