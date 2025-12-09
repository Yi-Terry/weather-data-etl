import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta




default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2025,4,30),
    'catchup':False,
}

dag = DAG(
    dag_id='weather-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5),  #updates every 5 minutes
    catchup=False
)


with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='',
        command='',
        working_dir='',
        Mounts=[],
        network_mode='',
        docker_url='',
        auto_remove=''
    )
    