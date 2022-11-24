from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator


def print_name_settings(name):
    return f"my name is {name}"

def print_name():
    return "my name is name"


default_args = {
    "owner": "klein",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

with DAG(dag_id="py_name",
         description="name",
         start_date=datetime(2022, 11, 23),
         schedule_interval="@daily",
         catchup=False,
         default_args=default_args
) as dg:
    task = PythonOperator(
        task_id="print_name",
        python_callable=print_name_settings,
        op_args="klein"
    )

    task2 = PythonOperator(
        task_id="print_name2",
        python_callable=print_name,
    )

task >> task2
