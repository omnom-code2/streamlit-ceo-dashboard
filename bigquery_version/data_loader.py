import streamlit as st
from google.cloud import bigquery, bigquery_storage
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def load_data():
  logging.info("Obtaining BigQuery configuration")
  service_account_info = st.secrets["bigquery"]
  logging.info("Creating a BigQuery client")
  client = bigquery.Client.from_service_account_info(service_account_info)
  logging.info("Getting the credentials")
  credentials = client._credentials
  logging.info("Creating a BigQuery Storage client")
  storage_client = bigquery_storage.BigQueryReadClient(credentials=credentials)
  logging.info("Getting the project ID")
  project_id = service_account_info["project_id"]
  logging.info("Creating the query string")
  query = f"select * from `{project_id}.sia_ceo_dashboard.sales_data`"
  logging.info("Executing the query")
  query_job = client.query(query)
  logging.info("Getting the query result")
  result = query_job.result()
  logging.info("Converting the result to a DataFrame")
  df = result.to_dataframe(bqstorage_client=storage_client)
  logging.info("Returning the DataFrame")
  return df