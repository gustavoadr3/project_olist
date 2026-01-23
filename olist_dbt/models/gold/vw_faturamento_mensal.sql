{{config(materialized = 'view')}}

with base_mensal as (
  select 
    c.ano,
    c.mes,
    sum(f.receita_item) as faturamento_mes,
    count(distinct f.id_pedido) as qtd_pedidos
  from {{ref ('fVendas')}} f
  left join {{ref ('dCalendario')}} c 
    on f.id_data = c.id_data
  where f.status_pedido = 'delivered'
  group by c.ano, c.mes
)

select
  ano,
  mes,
  faturamento_mes,
  qtd_pedidos,
  faturamento_mes / nullif(qtd_pedidos, 0) as ticket_medio
from base_mensal
order by ano, mes
