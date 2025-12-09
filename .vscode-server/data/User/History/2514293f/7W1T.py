from airflow import DAG
from datetime import datetime

default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2025,4,30),
    'catchup':False,

}

dag = DAG(
    dag_id = 'weather-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag: