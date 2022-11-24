from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import timedelta, datetime


default_args ={
    "owner" : "klein",
    "retries" : 2,
    "retry_delay" : timedelta(minutes= 1)
}


with DAG(
    dag_id= "postgres_operators",
    description="postgres operators test",
    start_date= datetime(2022, 11, 13),
    schedule_interval= "@daily",
    catchup= False,
    default_args= default_args
) as dg:
    task = PostgresOperator(
        task_id = "create table",
        postgres_conn_id= "DB_localhost",
        sql="./SQL/Create.sql" 
    )

    task