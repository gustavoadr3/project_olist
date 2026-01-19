select 
    p.product_id as id_produto,
    p.product_category_name as categoria_produto,
    p.product_weight_g as peso_produto_g,
    p.product_length_cm as comprimento_produto_cm,
    p.product_height_cm as altura_produto_cm,
    p.product_width_cm as largura_produto_cm
from {{ source('olist_silver', 'products') }} p
