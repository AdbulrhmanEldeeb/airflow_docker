from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
# airflow.providers.amazon.aws.sensors.s3.S3KeySensor
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

# {"aws_access_key_id":"cZtm2RaYMqypdHvzL1GZ","aws_secret_access_key":"T9ChGbof0ptGlki3kwXglCjyyup7M276XNjlY425",
#   "endpoint_url":"https://play.min.io:9000"
# }


with DAG(
    dag_id='dag_with_minio_s3_v02',
    start_date=datetime(2025, 3, 8),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='bucket1',
        #the file which the sensor waits for 
        bucket_key='data.csv',
        aws_conn_id='minio_conn',
        mode='poke',             
        poke_interval=5,      # it will scheck if the data is uploaded each 5 seconds 
        timeout=30            # 30 seconds 
    )