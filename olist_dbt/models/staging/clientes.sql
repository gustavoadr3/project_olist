select
    c.customer_id as id_cliente,
    c.customer_unique_id as id_cliente_unico,
    c.customer_zip_code_prefix as cep_cliente,
    c.customer_city as cidade_cliente,
    c.customer_state as estado_cliente
from {{ source('olist_silver', 'customers') }} c
