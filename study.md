## backfill
# لو انا عاوز اشغل ال داج من فترة محدةة ل فترة محددة ، شبه ال كاتشاب كده 
# to find scheduler container type the follwoing command and search for  (scheduler)
docker ps 

# then to execute schulder 
docker exec -it 4d2e94597514 bash 

airflow dags backfill -s 2025-03-02  -e 2025-03-04   dag_id
# ده علي سبيل المثال هيشتغل يوم 3و4و5
exit 