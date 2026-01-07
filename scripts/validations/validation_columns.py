from loguru import logger

def validate_columns(yaml_files: dict, csv_files: dict) -> bool:
    all_valid = True
    
    # Verifica se todas as tabelas do YAML existem no CSV
    for table_name in yaml_files:
        if table_name not in csv_files:
            logger.error(f'[Tabela: {table_name}] A tabela não está presente nos arquivos CSV')
            all_valid = False
            continue
        
        # Compara as colunas da tabela
        yaml_columns = set(yaml_files[table_name])
        csv_columns = set(csv_files[table_name])
        
        if yaml_columns != csv_columns:
            missing_in_csv = yaml_columns - csv_columns
            missing_in_yaml = csv_columns - yaml_columns
            
            if missing_in_csv:
                logger.error(f'[Tabela: {table_name}] Colunas faltando no CSV: {missing_in_csv}')
            
            if missing_in_yaml:
                logger.error(f'[Tabela: {table_name}] Colunas extras no CSV (não estão no YAML): {missing_in_yaml}')
            
            all_valid = False    
    # Verifica se há tabelas no CSV que não estão no YAML
    for table_name in csv_files:
        if table_name not in yaml_files:
            logger.warning(f'[Tabela: {table_name}] Tabela presente no CSV mas não definida no YAML')
    
    if all_valid:
        logger.info('Todas as colunas de todas as tabelas estão iguais')
    
    return all_valid