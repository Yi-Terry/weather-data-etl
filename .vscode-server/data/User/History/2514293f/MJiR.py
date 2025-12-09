import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    return main()


default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2025,4,30),
    'catchup':False,
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    description='Orchestrates weather API ingestion',
    default_args=default_args,
    schedule=timedelta(minutes=5),  #updates every 5 minutes
    catchup=False
)


with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )