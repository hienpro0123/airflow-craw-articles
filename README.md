# Crawl Data Project - Airflow & Docker Setup

## Overview
This project uses Apache Airflow to automate crawling the latest 10 articles and saving them into a PostgreSQL database.

## Setup Instructions

### Step 1: Build Docker Image
Open Docker and build the necessary image by running the provided `Dockerfile`.

### Step 2: Run Services with Docker Compose
Start all required services using docker-compose.yml.

### Step 3: Prepare Airflow DAGs and Application Functions
In the dags/ folder, make sure there is a new_dags.py file.
In the app/ folder, implement all three required functions for crawling and saving data.

### Step 4: Access Airflow Web Interface
Open http://localhost:8080.
Login with:
Username: airflow
Password: airflow
Find the DAG named crawl_data.
Click to manually trigger it and enable auto-scheduling.

### Step 5: Access Database Management Tool
Open http://localhost:5050.
Login with:
Username: admin@admin.com
Password: admin

### Step 6: Connect to the PostgreSQL Server
Add a new server connection (name it as you like).
Enter the connection details according to the reference image.

![PostgreSQL Connection Settings](https://i.imgur.com/kmhYCWC.png)

Save and query the articles table to verify the crawled data.

