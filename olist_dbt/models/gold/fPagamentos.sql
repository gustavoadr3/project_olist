select
    cast(pg.id_pedido as string) as id_pedido,
    cast(pg.sequencia_pagamento as int64) as sequencia_pagamento,
    cast(p.id_cliente as string) as id_cliente,
    cast(c.id_data as int64) as id_data,
    cast(pg.valor_pagamento as numeric) as valor_pagamento,
    1 as quantidade_pagamentos
from {{ ref('pagamentos') }} pg
join {{ ref('pedidos') }} p
  on pg.id_pedido = p.id_pedido
join {{ ref('dCalendario') }} c
  on date(p.data_compra) = c.data
