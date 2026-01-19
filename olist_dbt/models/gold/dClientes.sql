select 
    c.id_cliente
    ,c.id_cliente_unico
    ,c.cep_cliente
    ,UPPER(c.cidade_cliente) as cidade_cliente
    ,c.estado_cliente
from {{ref ("clientes")}} c