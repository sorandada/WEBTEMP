import pandas as pd
import datetime

glb_ave_temp = []
glo_count_temp_sum = []

def ndaysfunc(csv_file, sYear, sMonth, sDay, eYear, eMonth, eDay):
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



  hiku=datetime.datetime(eYear, eMonth, eDay)-datetime.datetime(sYear, sMonth, sDay)
  ndays=(hiku.days)+1

  days_temp = pd.DataFrame()  # 空

  for i in range(ndays):
      add_i_days=datetime.datetime(sYear, sMonth, sDay) + datetime.timedelta(days=i)

      # 1dayの指定
      day_temp = df_temp[(df_temp['day'] == add_i_days)]

      # 平均温度と平均温度の合計
      sum = 0
      count = 1
      start = day_temp["t"].index[0]  # 始まりのindexの番号
      end = day_temp["t"].index[-1] + 1  # おわりのindexの番号

      for i in range(start, end):
        if i == start:
          sum += day_temp.loc[start, "t"]
        else:
          sum += day_temp.loc[i, "t"]
          count += 1

      global glb_ave_temp  # 平均温度が上書きされる
      glb_ave_temp = sum / count

      global glb_count_temp_sum  # 温度の合計が上書きされる
      glb_count_temp_sum = sum

      # indexの変更
      day_temp.set_index("__time", inplace=True)
      # 時系列を直す
      day_temp = day_temp[::-1]



      if ndays == 0:
          days_temp = day_temp

      else:
          days_temp = pd.concat([days_temp, day_temp], axis=0)

  return days_temp


def tempave():
    return  glb_ave_temp

def tempsumcount():
  return  glb_count_temp_sum
