from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from external_api_call.utils import (
    fetch_todos,
    load_todos,
    fetch_albums,
    load_albums,
    fetch_posts,
    load_posts,
)


default_args = {
    "owner": "mobin",
    "depends_on_past": False,
    "start_date": datetime(2024, 12, 1),
    "email": ["aalmobin8@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    "fetch-data-from-jsonplaceholer-dag",
    default_args=default_args,
    schedule_interval=timedelta(1),
)

t1 = PythonOperator(
    task_id="fetch_todos",
    provide_context=True,
    python_callable=fetch_todos,
    dag=dag,
)


t2 = PythonOperator(
    task_id="load_todos",
    provide_context=True,
    python_callable=load_todos,
    dag=dag,
)


t3 = PythonOperator(
    task_id="fetch_albums",
    provide_context=True,
    python_callable=fetch_albums,
    dag=dag,
)

t4 = PythonOperator(
    task_id="load_albums",
    provide_context=True,
    python_callable=load_albums,
    dag=dag,
)

t5 = PythonOperator(
    task_id="fetch_posts",
    provide_context=True,
    python_callable=fetch_posts,
    dag=dag,
)

t6 = PythonOperator(
    task_id="load_posts",
    provide_context=True,
    python_callable=load_posts,
    dag=dag,
)


t2.set_upstream(t1)
t4.set_upstream(t3)
t6.set_upstream(t5)
