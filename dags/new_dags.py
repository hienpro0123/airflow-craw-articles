import sys
from pathlib import Path
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
# Fix import path
dag_path = Path(__file__).parent.absolute()
project_path = dag_path.parent
sys.path.append(str(project_path))

from app.crawl_news import crawl_data
from app.clean_data import cleaned_data
from app.insert_to_postgres import insert_data_to_database

# Tạo DAG
dag = DAG(
    'crawl_data',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 10 * * *',
    catchup=False
)

# Task data_task: Thu thập, xử lý và lưu dữ liệu
def data_task():
    data = crawl_data()  # Thu thập dữ liệu từ crawl_data() 
    data_transformed = cleaned_data(data)  # Biến đổi dữ liệu từ cleaned_data.py
    insert_data_to_database(data_transformed)  # Lưu vào DB từ insert_to_postgres.py

# Tạo PythonOperator cho task
data_duty = PythonOperator(
    task_id='data',
    python_callable=data_task,
    dag=dag,
)

# Thiết lập thứ tự thực thi (ở đây chỉ có một task)
data_duty
