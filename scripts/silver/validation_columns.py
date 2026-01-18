import pandas as pd 
from pandas import DataFrame
from typing import Callable
from loguru import logger

def validation_coluns(func_read: Callable, client_json: str, func_yaml: Callable, path_yaml: str) -> DataFrame:
    try:

        configs = func_yaml(path=path_yaml)     
        df = func_read(configs=configs, auth_gcp=client_json)
        coluns_out = []       
        extra_columns = []    
        type_errors = [] 
        null_errors = []
        yaml_names = []

        for col_config in configs['columns']:
            yaml_names.append(col_config['name'])

        for df_col in df.columns:
            if df_col not in yaml_names:
                extra_columns.append(df_col)
        
        if extra_columns:
            logger.warning(f"Colunas extras removidas: {extra_columns}")
            df = df.drop(columns=extra_columns)

        for col_config in configs['columns']:
            name = col_config['name']
            expected_type = str(col_config['type']).lower()
            is_nullable = col_config.get('nullable', True) 

            if name not in df.columns:
                coluns_out.append(name)
            else:
                if not is_nullable:
                    if df[name].isnull().any():
                        qtd_nulos = df[name].isnull().sum()
                        null_errors.append(f"{name}: possui {qtd_nulos} valores nulos")

                if expected_type == "timestamp":
                    try:
                        df[name] = pd.to_datetime(df[name])
                    except Exception:
                        type_errors.append(f"{name}: falha na conversao para TIMESTAMP")
                
                else:
                    actual_type = str(df[name].dtype)
                    if actual_type != expected_type:
                        try:
                            df[name] = df[name].astype(expected_type)    
                        except Exception:
                            type_errors.append(f"{name}: erro de conversao {actual_type} -> {expected_type}")

        if coluns_out:
            logger.error(f"Colunas ausentes: {coluns_out}")

        if null_errors:
            logger.error(f"Campos obrigatórios com valores nulos: {null_errors}")

        if type_errors:
            logger.error(f"Erros de tipo/conversão: {type_errors}")
        
        return df

    except Exception as e:
        logger.error(f'Erro crítico na validação: {e}')