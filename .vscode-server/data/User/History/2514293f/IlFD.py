from airflow import DAG

DAG(
    dag_id = 'weather-api-orchestrator',
    default_args=default_args
)