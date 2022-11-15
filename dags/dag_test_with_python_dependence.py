from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def get_version():
    import sklearn
    return f"this is the version of sklearn{sklearn.__version__}"


def get_other_version():
    import numpy, pandas, matplotlib
    print(f"this is older version of \n numpy=={numpy.__version__}\npandas=={pandas.__version__}\nmatplotlib=={matplotlib.__version__}")


default_args = {
    "owner": "klein",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
        dag_id="python_dependences",
        description=" get a python dependence",
        start_date=datetime(2022, 11, 15),
        schedule_interval="@daily",
        catchup=False,
        default_args=default_args
) as dg:
    print_version = PythonOperator(
        task_id="task1",
        python_callable=get_version,

    )
    oder_version = PythonOperator(
        task_id="task2",
        python_callable=get_version,

    )


print_version >> oder_version