from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import timedelta, datetime

default_args = {
    "owner": "klein",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
        dag_id="Postgres_Data",
        description="import a data on postgres server",
        start_date=datetime(2022, 11, 24),
        schedule_interval="@daily",
        catchup=False,
        default_args=default_args
) as dg:
    Create = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="DB_ytb",
        sql="SQL/CreateDagTable.sql"
    )

    selection = PostgresOperator(
        task_id="select_data",
        postgres_conn_id="DB_ytb",
        sql="""
        SELECT * FROM COMMENTS
        WHERE textDisplay LIKE '%Merci%';
        """
    )

Create >> selection

