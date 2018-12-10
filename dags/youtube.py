from datetime import datetime, timedelta, timezone
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

dag = DAG('youtube3',
          default_args=default_args,
          schedule_interval='*/1 * * * *',
          start_date=datetime(2018, 12, 3, 15, 20, 0, 0))

t1 = SimpleHttpOperator(
    task_id='trigger_ingestion',
    http_conn_id='http_youtube_ingestor',
    endpoint='/',
    method='GET',
    log_response=True,
    dag=dag,
)

t1
