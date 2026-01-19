select
    o.order_id as id_pedido,
    o.order_item_id as id_item_pedido,
    o.product_id as id_produto,
    o.seller_id as id_vendedor,
    cast(o.shipping_limit_date as timestamp) as data_limite_envio,
    cast(o.price as numeric) as preco,
    cast(o.freight_value as numeric) as valor_frete
from {{ source('olist_silver', 'orders_items') }} o
