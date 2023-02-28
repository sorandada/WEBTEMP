import streamlit as st
import pandas as pd

import datetime

import func
import ndays
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

    df = (func.tempfanc_df('440103227943283_7.csv', sYear, sMonth, sDay))
    df = pd.DataFrame(df[["t"]])
    st.title("Table")
    st.dataframe(df.T)

    st.title("TempData_Statistics")
    st.dataframe(df.describe().T)

    st.title("Graf")
    st.line_chart(data=df, x=None, y="t", width=1000, height=500, use_container_width=True)

    st.header("・"+str(s_day)+ " TempAverage[t] is " + str(sum(df["t"]) / len(df["t"])) + "℃")



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
    df = (ndays.ndaysfunc('440103227943283_7.csv', sYear, sMonth, sDay, eYear, eMonth, eDay))
    df = pd.DataFrame(df[["t"]])

    st.dataframe(df.T)

    st.title("TempData_Statistics")
    st.dataframe(df.describe().T)



    st.title("Graf")
    st.line_chart(data=df, x=None, y="t", width=1000, height=500, use_container_width=True)


    n_day_ago=e_day+datetime.timedelta(days=1) - s_day

    full_sum = 0
    days_sum = 0
    count=0
    df_days = pd.DataFrame()  # 空
    for i in range(n_day_ago.days):
        ans=0
        c=0
        for v in df.index.values:
            if str(s_day+datetime.timedelta(days=i)) in v:
                ans += float(df.loc[[v]]["t"])
                c+=1
        count+=1

        full_sum = ans / c #平均温度

        days_sum += full_sum #平均温度の合計

        col=[]
        sum_ave_temp =[]

        df_day=pd.DataFrame([ans, c, full_sum, days_sum],
                     index=['"温度の合計', '測定された温度回数', '平均温度', '平均温度の合計'],
                     columns=[s_day + datetime.timedelta(days=i)])

        col.append(s_day + datetime.timedelta(days=i))
        sum_ave_temp.append(days_sum)


        df_days = pd.concat([df_days, df_day], axis=1)



    st.dataframe(df_days)


    st.title(str(s_day) + "～" + str(e_day) + "間の平均温度合計")
    st.title(">>>" + str(days_sum))
    st.title(str(s_day) + "～" + str(e_day) + "間の平均温度合計の平均")
    st.title(">>>"+str(days_sum/count))


