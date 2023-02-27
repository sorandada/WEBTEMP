import pandas as pd
import numpy as np
import datetime as dt
import datetime

#import main
#print(main.s_day)


def tempfanc(csv_file, sYear, sMonth, sDay):
  df_temp = pd.read_csv(csv_file)

  l=[]
  l_d=[]
  for i in range(len(df_temp.columns)):
    l.append(df_temp.columns[i])
    if df_temp.columns[i]!='__time':
      if df_temp.columns[i]!='t':
        l_d.append(df_temp.columns[i])

  df_temp=df_temp.drop(l_d, axis=1)

  df_temp['day']  = df_temp['__time'].str.split(pat=' ', expand=True)[0]
  df_temp['time']  = df_temp['__time'].str.split(pat= ' ', expand=True)[1]

  df_temp.isnull().sum()

  df_temp['day'] = pd.to_datetime(df_temp['day'])

  #day_temp=df_temp[(df_temp['day'] == dt.datetime(2023, 2, 1))]
  day_temp = df_temp[(df_temp['day'] == datetime.datetime(sYear, sMonth, sDay))]#############################################
  #print(day_temp["t"])
  #print(day_temp.describe())

  # ここから　日にちごとのスタートからの平均温度
  temp_sum = []
  temp_sum_ave = []
  inDex=[]
  sum = 0
  count = 1
  start = day_temp["t"].index[0]
  end = day_temp["t"].index[-1] + 1

  for i in range(start, end):
    if i == start:
      temp_sum.append(day_temp.loc[start, "t"])
      temp_sum_ave.append(day_temp.loc[start, "t"] / count)
      sum += day_temp.loc[start, "t"]
      inDex.append(start)
    else:
      sum += day_temp.loc[i, "t"]
      count += 1
      temp_sum.append(sum)
      temp_sum_ave.append(sum / count)
      start+=1
      inDex.append(start)

  temp_sum_ave = pd.DataFrame(temp_sum_ave)
  temp_sum_ave = temp_sum_ave.rename(columns={0: "t_ave"})
  inDex = pd.DataFrame(inDex)
  inDex = inDex.rename(columns={0: "number"})
  temp_sum_ave = pd.concat([temp_sum_ave, inDex], axis=1)
  temp_sum_ave.set_index("number", inplace=True)
  #print(temp_sum_ave)

  day_temp = pd.concat([day_temp, temp_sum_ave], axis=1)

  """day_temp = day_temp.rename(columns={0: "t_ave"})"""

  #indexの変更
  day_temp.set_index("__time", inplace=True)

  return day_temp

"""s_day=dt.datetime(2023, 2, 1)
day_temp=tempfanc('440103227943283_7.csv', s_day)
df=pd.DataFrame(day_temp)
print(df)"""





