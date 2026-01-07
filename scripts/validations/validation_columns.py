from loguru import logger

def validate_columns(yaml_files: dict, csv_files: dict) -> bool:
    if yaml_files == csv_files:
        logger.info('Todas as colunas estáo iguais')
        return True
    else:
        logger.error('As colunas são diferentes')
        return False