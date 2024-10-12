import streamlit as st
from data_wrangling import get_filtered_data_within_date_range, prep_data
from filter_panel import filter_panel
from date_range_panel import date_range_panel
from metric_bar import metric_bar
from time_series_chart import time_series_chart
from pie_chart import pie_chart

st.set_page_config(layout='wide')

with st.sidebar:
  start, end = date_range_panel()

data = prep_data()
filters = filter_panel(data)

main_df = get_filtered_data_within_date_range(data, start, end, filters)
if main_df.empty:
  st.warning("No data to display")
else:
  metric_bar(main_df)
  time_series_col, pie_chart_col = st.columns(2)
  with time_series_col:
    time_series_chart(main_df)
  with pie_chart_col:
    pie_chart(main_df)
