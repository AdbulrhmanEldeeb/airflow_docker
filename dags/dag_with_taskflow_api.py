from datetime import datetime, timedelta
from airflow.decorators import dag, task
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# >> is not needed in TaskFlow API 

@dag(dag_id='dag_with_taskflow_api_v10', 
     default_args=default_args, 
     start_date=datetime(2025, 2, 27), 
     schedule_interval='@daily',
    # it starts to process all dags before the current date and after start date to finish them as soon as possible
    #  the catchup disables this 
     catchup=False,
     )
def hello_world_etl(): 

    @task(multiple_outputs=True)
    def get_info(): 
        return {
            "name": "abdo01",
            "age": 22
        }

    @task
    def get_job(): 
        return "engineer"

    @task
    def show_info(name, age, job): 
        print(f"hello i am {name}, I work as an {job}, and I am {age} years old")

    # Call tasks correctly
    info = get_info()
    job = get_job() 
    show_info(info["name"], info["age"], job)

greet = hello_world_etl()
