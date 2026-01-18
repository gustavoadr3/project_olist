import pandas as pd
from pandas import DataFrame
from typing import Dict


def read_bucket(configs: Dict, auth_gcp: str) -> DataFrame: 
    table = configs["table"]
    source = configs["load"]
    source = source["source"]
    type = source["format"]
    path_gcp = source["path"]
    name_table = table["name"]
    path = f"{path_gcp}{name_table}.{type}"
    df = pd.read_csv(path,
                    storage_options= {
                        "token": auth_gcp
                    })
    return df