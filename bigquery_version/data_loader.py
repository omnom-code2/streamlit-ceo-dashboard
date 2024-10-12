import streamlit as st
from google.cloud import bigquery

def load_data():
  service_account_info = st.secrets["bigquery"]
  client = bigquery.Client.from_service_account_info(service_account_info)
  project_id = service_account_info["project_id"]
  query = f"select * from `{project_id}.sia_ceo_dashboard.sales_data`"
  query_job = client.query(query)
  result = query_job.result()
  return result.to_dataframe()