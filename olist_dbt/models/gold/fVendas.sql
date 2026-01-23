select
    i.id_pedido,
    i.id_item_pedido,
    p.id_cliente,
    i.id_produto,
    i.id_vendedor,
    p.status_pedido,
    c.id_data,
    i.preco,
    i.valor_frete,
    i.preco + i.valor_frete as receita_item,
    1 as quantidade
from {{ ref('itens_pedidos') }} i
join {{ ref('pedidos') }} p
  on i.id_pedido = p.id_pedido
join {{ ref('dCalendario') }} c
  on date(p.data_compra) = c.data
