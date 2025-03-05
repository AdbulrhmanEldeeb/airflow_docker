from datetime import datetime, timedelta
from airflow.decorators import task
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook

POSTGRES_CONN_ID="postgres_conn"
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_postgres_operator_v022',
    default_args=default_args,
    start_date=datetime(2025, 2, 19),
    schedule_interval='0 0 * * *',
    catchup=False
) as dag:
    @task
    def create_table():
        """Load transformed data into PostgreSQL."""
        try:
            pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
            conn = pg_hook.get_conn()
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS i_succeded (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            print("~~~~~~~~~~~created table succesfully~~~~~~~~~~~")
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

    create_table()

