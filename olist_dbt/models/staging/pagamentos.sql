select 
    op.order_id as id_pedido,
    cast(op.payment_sequential as integer) as sequencia_pagamento,
    op.payment_type as tipo_pagamento,
    cast(op.payment_installments as integer) as pagamento_parcelado,
    cast(op.payment_value as numeric) as valor_pagamento 
from {{ source('olist_silver', 'order_payments') }} op
