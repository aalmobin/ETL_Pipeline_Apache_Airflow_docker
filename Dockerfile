FROM apache/airflow:2.10.3-python3.12
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt