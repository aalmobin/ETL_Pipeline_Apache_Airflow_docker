# ETL Project Using Apache Airflow
## Initialize the database
### On all operating systems, you need to run database migrations and create the first user account. To do this, run.
```bash
docker-compose up airflow-init
```
### After initialization is complete, you should see a message like this:
```bash
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.10.3
start_airflow-init_1 exited with code 0
```
### Now you can start all services:
```bash
docker-compose up
```
## Cleaning up
### To stop and delete containers, delete volumes with database data and download images, run:
```bash
docker-compose down --volumes --rmi all
```