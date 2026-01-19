select 
    s.seller_id as id_vendedor,
    s.seller_zip_code_prefix as cep_vendedor,
    s.seller_city as cidade_vendedor,
    s.seller_state as estado_vendedor
from {{ source('olist_silver', 'sellers') }} s
