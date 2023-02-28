import pandas as pd
import datetime


glb_ave_temp = 0
glo_count_temp_sum = 0
def tempfanc_df(csv_file, sYear, sMonth, sDay):
  df_temp = pd.read_csv(csv_file)

  #df_temp = df_temp.iloc[::-1]

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


  #1dayの指定
  day_temp=df_temp[(df_temp['day'] == datetime.datetime(sYear, sMonth, sDay))]

  # 平均温度と平均温度の合計
  sum = 0
  count = 1
  start = day_temp["t"].index[0] #始まりのindexの番号
  end = day_temp["t"].index[-1] + 1 #おわりのindexの番号

  for i in range(start, end):
    if i == start:
      sum += day_temp.loc[start, "t"]
    else:
      sum += day_temp.loc[i, "t"]
      count += 1


  global glb_ave_temp #平均温度が上書きされる
  glb_ave_temp =sum/count

  global glb_count_temp_sum  # 温度の合計が上書きされる
  glb_count_temp_sum = sum



  #indexの変更
  day_temp.set_index("__time", inplace=True)
  #時系列を直す
  day_temp = day_temp[::-1]

  return day_temp


def tempave():
  return  glb_ave_temp

def tempsumcount():
  return  glb_count_temp_sum



