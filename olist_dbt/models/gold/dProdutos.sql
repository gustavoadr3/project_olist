select 
    p.id_produto,
    replace(p.categoria_produto, '_', ' ') as categoria_produto,
    cast(p.peso_produto_g as numeric) as peso_produto_g,
    cast(p.comprimento_produto_cm as numeric) as comprimento_produto_cm,
    cast(p.altura_produto_cm as numeric) as altura_produto_cm,
    cast(p.largura_produto_cm as numeric) as largura_produto_cm
from {{ ref('produtos') }} p
