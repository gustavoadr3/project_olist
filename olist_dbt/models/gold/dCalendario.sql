with datas_base as (

    select
        min(date(data_compra)) as data_min,
        max(date(data_compra)) as data_max
    from {{ ref('pedidos') }}

),

datas as (

    select
        data
    from datas_base,
    unnest(
        generate_date_array(data_min, data_max)
    ) as data

)

select
    cast(format_date('%Y%m%d', data) as int64) as id_data,
    data,
    extract(year from data) as ano,
    extract(month from data) as mes,

    case extract(month from data)
        when 1 then 'Janeiro'
        when 2 then 'Fevereiro'
        when 3 then 'Março'
        when 4 then 'Abril'
        when 5 then 'Maio'
        when 6 then 'Junho'
        when 7 then 'Julho'
        when 8 then 'Agosto'
        when 9 then 'Setembro'
        when 10 then 'Outubro'
        when 11 then 'Novembro'
        when 12 then 'Dezembro'
    end as nome_mes,

    extract(quarter from data) as trimestre,
    extract(day from data) as dia,

    extract(dayofweek from data) as dia_semana,

    case extract(dayofweek from data)
        when 1 then 'Domingo'
        when 2 then 'Segunda-feira'
        when 3 then 'Terça-feira'
        when 4 then 'Quarta-feira'
        when 5 then 'Quinta-feira'
        when 6 then 'Sexta-feira'
        when 7 then 'Sábado'
    end as nome_dia_semana,

    extract(week from data) as semana_ano,

    case
        when extract(dayofweek from data) in (1, 7) then true
        else false
    end as fim_de_semana

from datas
order by data

