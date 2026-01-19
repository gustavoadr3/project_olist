select
    o.order_id as id_pedido,
    o.customer_id as id_cliente,
    o.order_status as status_pedido,
    cast(o.order_purchase_timestamp as timestamp) as data_compra,
    cast(o.order_approved_at as timestamp) as data_aprovacao,
    cast(o.order_delivered_carrier_date as timestamp) as data_envio_transportadora,
    cast(o.order_delivered_customer_date as timestamp) as data_entrega_cliente,
    cast(o.order_estimated_delivery_date as timestamp) as data_prevista_entrega
from {{ source('olist_silver', 'orders') }} o
