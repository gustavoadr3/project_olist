select 
    v.id_vendedor
    ,v.cep_vendedor
    ,UPPER(v.cidade_vendedor) as cidade_vendedor
    ,v.estado_vendedor
from {{ref ("vendedores")}} v