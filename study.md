## backfill
# لو انا عاوز اشغل ال داج من فترة محدةة ل فترة محددة ، شبه ال كاتشاب كده 
# to find scheduler container type the follwoing command and search for  (scheduler)
docker ps 

# then to execute schulder 
docker exec -it 4d2e94597514 bash 

airflow dags backfill -s 2025-03-02  -e 2025-03-04   dag_id
# ده علي سبيل المثال هيشتغل يوم 3و4و5
exit 


# to connect to postgres database 
host a postgres database and get it's credintials (avien gives free postgress databases)
edit docker-compose the following section for your credintials (use help of llm)
    ```
    services:
    postgres:
        image: postgres:13
        environment:
        POSTGRES_USER: avnadmin
        POSTGRES_PASSWORD: ${avien_postegres_password}
        POSTGRES_DB: defaultdb
        ports:
        - "22114:5432"
        healthcheck:
        test: ["CMD", "pg_isready", "-U", "avnadmin"]
        interval: 10s
        retries: 5
        start_period: 5s
        restart: always
    ```
create a connection in admin in the airflow ui 
modify the dag py file to include the connection_id 
test dag

## 2- run to rebuild 
docker-compose up -d --no-deps --build postgres        
where postgres is the service name in the docker-compose.yml 


