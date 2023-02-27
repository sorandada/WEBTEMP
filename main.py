import streamlit as st
import pandas as pd
import numpy as np
import datetime

import func
st.set_page_config(layout="wide")
pagelist = ["1日の温度","N日間の温度"]

selector=st.sidebar.radio( "ページ選択",pagelist)
if selector=="1日の温度":
    st.sidebar.title("平均気温")
    st.sidebar.title("カレンダーから選択")

    s_day = st.sidebar.date_input(
        "ここから",
        datetime.datetime(2023, 2, 1))
    st.sidebar.write('start_day', s_day)

    sYear = s_day.year
    sMonth = s_day.month
    sDay = s_day.day

    st.title("Table")
    df = (func.tempfanc('440103227943283_7.csv', sYear, sMonth, sDay))

    df = pd.DataFrame(df[["t", "t_ave"]])

    st.dataframe(df.T)

    st.title("TempData_Statistics")
    st.dataframe(df.describe().T)

    st.title("Graf")
    st.line_chart(data=df, x=None, y=("t", "t_ave"), width=1000, height=500, use_container_width=True)

    st.header("・"+str(s_day)+ " TempAverage[t] is " + str(sum(df["t"]) / len(df["t"])) + "℃")
    st.header("・"+str(s_day)+ " TempAverage[t_ave] is " + str(sum(df["t_ave"]) / len(df["t_ave"])) + "℃")


    c = 0
    for v in df.index.values:
        if str(s_day) in v:
            c += 1
    ans=0
    full_ans=0
    for v in df.index.values:
        if str(s_day) in v:
            ans+=float(df.loc[[v]]["t"])
    st.title(ans/c)
    ans=0

    sYear = s_day.year
    sMonth = s_day.month
    sDay = s_day.day
elif selector=="N日間の温度":
    st.sidebar.title("平均気温")
    st.sidebar.title("カレンダーから選択")

    s_day = st.sidebar.date_input(
        "ここから",
        datetime.datetime(2023, 2, 1))
    st.sidebar.write('start_day', s_day)

    sYear = s_day.year
    sMonth = s_day.month
    sDay = s_day.day

    e_day = st.sidebar.date_input(
        "ここまで",
        datetime.datetime(2023, 2, 1))
    st.sidebar.write('end_day', e_day)

    eYear = e_day.year
    eMonth = e_day.month
    eDay = e_day.day

    st.title("Table")
    df = (func.tempfanc('440103227943283_7.csv', sYear, sMonth, sDay, eYear, eMonth, eDay))
    df = pd.DataFrame(df[["t", "t_ave"]])

    st.dataframe(df.T)

    st.title("TempData_Statistics")
    st.dataframe(df.describe().T)



    st.title("Graf")
    st.line_chart(data=df, x=None, y=("t", "t_ave"), width=1000, height=500, use_container_width=True)



    st.header("・"+str(s_day) + "～" + str(e_day) + " TempAverage[t] is " + str(sum(df["t"])/len(df["t"])) + "℃")
    st.header("・"+str(s_day) + "～" + str(e_day) + " TempAverage[t_ave] is " + str(sum(df["t_ave"])/len(df["t_ave"])) + "℃")

    n_day_ago=e_day+datetime.timedelta(days=1) - s_day
    #st.title(n_day_ago.days)

    #st.title(s_day)

    full_sum = 0
    for i in range(n_day_ago.days):
        ans=0
        c=0
        for v in df.index.values:
            if str(s_day+datetime.timedelta(days=i)) in v:
                #st.title(df[s_day + datetime.timedelta(days=i)]["t"])
                ans += float(df.loc[[v]]["t"])
                c+=1

        st.title("#################################")
        st.title(s_day + datetime.timedelta(days=i))
        st.write("合計：", str(ans))
        st.write("個数：", str(c))
        st.write("ave:", str(ans/c))

        full_sum += ans / c
        st.write("day_temp_ave_sum:", str(full_sum))

    st.title(str(s_day) + "～" + str(e_day) + "間の平均温度合計")
    st.title(">>>" + str(full_sum))
    st.title(str(s_day) + "～" + str(e_day) + "間の平均温度合計の平均")
    st.title(">>>"+str(full_sum/int(n_day_ago.days)))


