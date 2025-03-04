from airflow import DAG 
from airflow.operators.python import PythonOperator 
from datetime import timedelta,datetime
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# xcom can not carry data bigger than 48 kp , like pandas dataframes 


# task instance 
def greet(ti):
    first_name=ti.xcom_pull(task_ids="GET_NAME_task",key="first_name")
    last_name=ti.xcom_pull(task_ids="GET_NAME_task",key="last_name")
    age=ti.xcom_pull(task_ids="get_age_task",key="age")
    print(f"hello i am greet, my name is {first_name} {last_name} and my age is {age}")

def get_name_1(ti): 
      ti.xcom_push(key="first_name",value="abdo")
      ti.xcom_push(key="last_name",value="eldeeb")

def get_age(ti):
      ti.xcom_push(key="age",value=22)
with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v06',
    description='Our first dag using python operator',
    start_date=datetime(2025, 3, 1),
    schedule_interval='@daily'
) as dag:
        task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={"name":"abdo","age":22}
    )
    
        task2 = PythonOperator(
        task_id='GET_NAME_task',
        python_callable=get_name_1,
        # op_kwargs={"name":"abdo","age":22}
    )
        task3=PythonOperator(
        task_id="get_age_task",
        python_callable=get_age,
        )
        [task2,task3 ]>> task1
    