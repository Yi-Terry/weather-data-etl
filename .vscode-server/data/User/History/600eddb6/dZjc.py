import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount



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
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        Mounts=[
           Mount(source='/home/terry/repos/weather-data-project/dbt/my_project',
                 target='/usr/app',
                 type='bind'),
            Mount(source='/home/terry/repos/weather-data-project/dbt',
                 target='/root/.dbt',
                 type='bind')
        ],
        network_mode='my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )