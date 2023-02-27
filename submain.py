import streamlit as st
import pandas as pd
import numpy as np

import sublesson


st.sidebar.title("平均気温")
st.sidebar.title("カレンダーから選択")
import datetime as dt
import datetime

s_day = st.sidebar.date_input(
    "ここから",
    datetime.datetime(2023, 2, 1))
st.sidebar.write('start_day', s_day)

sYear=s_day.year
sMonth=s_day.month
sDay=s_day.day

e_day = st.sidebar.date_input(
    "ここまで",
    dt.datetime(2022, 2, 2))
st.sidebar.write('end_day', e_day)


st.title("Table")
df=(lessonapi.tempfanc('440103227943283_7.csv', sYear, sMonth, sDay))
df=pd.DataFrame(df)

st.dataframe(df.T)

st.title("TempData_Statistics")
st.dataframe(df.describe().T)


st.title("Graf")
st.line_chart(data=df, x=None, y=("t","t_ave"), width=1000, height=500, use_container_width=True)


st.header(str(s_day)+"～"+str(e_day)+" TempAverage[t] is "+str(00)+"℃")
st.header(str(s_day)+"～"+str(e_day)+" TempAverage[t_ave] is "+str(00)+"℃")










