{{config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select *
    from {{source('dev', 'raw_weather_data')}}
)
select  
    