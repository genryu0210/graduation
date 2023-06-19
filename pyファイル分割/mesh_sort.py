# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:49:41 2021

@author: ktaka
"""
# In[モジュールのimport]


import openpyxl
import os
import zipfile
import numpy as np
import pandas as pd
from datetime import datetime, date, timezone, timedelta
import datetime
import seaborn as sns
from sklearn.linear_model import LinearRegression
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import japanize_matplotlib
import math
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from csv import reader
import pickle
from matplotlib.ticker import FormatStrFormatter

# In[]

#CSV読み込み
df1 = pd.read_csv("clearpoint.csv",encoding = "shift-jis")
#メッシュコードのみリスト化
mesh_list = df1["code"].tolist()
#メッシュコード取得
mesh_code = mesh_list[0] #6441427950#
get_mesh_code = str(mesh_code - 6441000000)
#規則に従い変換左右の移動と上下の移動に分ける
lr = int(get_mesh_code[-6])*100+int(get_mesh_code[-4])*10+int(get_mesh_code[-2])
ud = int(get_mesh_code[-5])*100+int(get_mesh_code[-3])*10+int(get_mesh_code[-1])

lr_m_list = []
ud_n_list = []
#2km左右上下のみ移動した際の番号を取得
for i in range (41):
    lr_m = lr -20 + i
    lr_m_list.append(lr_m)
    ud_n = ud -20 + i
    ud_n_list.append(ud_n)
    
cols = ['lr_m', 'ud_n']
#すべての組み合わせを作成
lr_m_list_todf =[]
ud_n_list_todf =ud_n_list*41

for i in range(len(lr_m_list)):
    for n in range(len(lr_m_list)):
        m = lr_m_list[i]
        lr_m_list_todf.append(m)  
#データフレームに格納
df2 = pd.DataFrame(list(zip(lr_m_list_todf,ud_n_list_todf)), columns = ['lr_m', 'ud_n'])
#マンハッタン距離の取得
df2["distance"] = (abs(df2['lr_m'] - lr) + abs(df2['ud_n'] - ud))
#マンハッタン距離2km以上の組み合わせを除外
df3 = df2[df2["distance"] < 21]
#マンハッタン距離が短い順にソート
df3 = df3.sort_values("distance")
df3 = df3.reset_index(drop=True)

lr_re_list = df3["lr_m"].tolist()
ud_re_list = df3["ud_n"].tolist()

distanse_list = df3["distance"].tolist()
#メッシュコードに再変換
search_code = []

for i in range(len(df3)):
    search_code.append(6441000000 + int(str(lr_re_list[i])[-1])*10 + int(str(lr_re_list[i])[-2])*1000 + int(str(lr_re_list[i])[-3])*100000 + int(str(ud_re_list[i])[-1]) + int(str(ud_re_list[i])[-2])*100 + int(str(ud_re_list[i])[-3])*10000)
#メッシュコードと距離を格納したデータフレームを出力
df4 = pd.DataFrame(list(zip(search_code,distanse_list)), columns = ['search_code', 'distanse_list'])

df4.to_csv("df4.csv")

# In[全メッシュについて実行して結果をリストに格納して保存]

#CSV読み込み
df1 = pd.read_csv("clearpoint.csv",encoding = "shift-jis")
#メッシュコードのみリスト化
mesh_list = df1["code"].tolist()
#メッシュコード取得
sort_list = []
for z in range(len(mesh_list)):
    mesh_code = mesh_list[z]
    get_mesh_code = str(mesh_code - 6441000000)
    #規則に従い変換左右の移動と上下の移動に分ける
    lr = int(get_mesh_code[-6])*100+int(get_mesh_code[-4])*10+int(get_mesh_code[-2])
    ud = int(get_mesh_code[-5])*100+int(get_mesh_code[-3])*10+int(get_mesh_code[-1])
    
    lr_m_list = []
    ud_n_list = []
    #2km左右上下のみ移動した際の番号を取得
    for i in range (41):
        lr_m = lr -20 + i
        lr_m_list.append(lr_m)
        ud_n = ud -20 + i
        ud_n_list.append(ud_n)
        
    cols = ['lr_m', 'ud_n']
    #すべての組み合わせを作成
    lr_m_list_todf =[]
    ud_n_list_todf =ud_n_list*41
    
    for i in range(len(lr_m_list)):
        for n in range(len(lr_m_list)):
            m = lr_m_list[i]
            lr_m_list_todf.append(m)  
    #データフレームに格納
    df2 = pd.DataFrame(list(zip(lr_m_list_todf,ud_n_list_todf)), columns = ['lr_m', 'ud_n'])
    #マンハッタン距離の取得
    df2["distance"] = (abs(df2['lr_m'] - lr) + abs(df2['ud_n'] - ud))
    #マンハッタン距離2km以上の組み合わせを除外
    df3 = df2[df2["distance"] < 21]
    #マンハッタン距離が短い順にソート
    df3 = df3.sort_values("distance")
    df3 = df3.reset_index(drop=True)
    
    lr_re_list = df3["lr_m"].tolist()
    ud_re_list = df3["ud_n"].tolist()
    
    distanse_list = df3["distance"].tolist()
    #メッシュコードに再変換
    search_code = []
    
    for i in range(len(df3)):
        search_code.append(6441000000 + int(str(lr_re_list[i])[-1])*10 + int(str(lr_re_list[i])[-2])*1000 + int(str(lr_re_list[i])[-3])*100000 + int(str(ud_re_list[i])[-1]) + int(str(ud_re_list[i])[-2])*100 + int(str(ud_re_list[i])[-3])*10000)
    #メッシュコードと距離を格納したデータフレームを出力
    df4 = pd.DataFrame(list(zip(search_code,distanse_list)), columns = ['search_code', 'distanse_list'])
    sort_list.append(df4)
    print(mesh_code)
    

with open("./sort_list.pickle", "wb") as f:
    pickle.dump(sort_list,f)
    
    
# In[xをロード]    

with open("./sort_list.pickle", "rb") as f:
    x = pickle.load(f)
    
    
# In[距離表を出す]
distances = list()
for n in range(len(x)):
    dfx =x[n]
    print(dfx.iloc[0,0])
    df5 = pd.merge(dfx, df1, left_on='search_code', right_on=['code'], how='inner')


    for i in range(len(df5)):
        if df5["病院の数"][i] > 0:
            distances.append(df5["distanse_list"][i]) 
            print(distances[n]) 
            break
        elif i == len(df5)-1 and df5["病院の数"][i] == 0:
            distances.append(20) 
            # print(distances[n]) 
            break
        else:
            pass



with open("./distances.pickle", "wb") as f:
    pickle.dump(distances,f)
np.savetxt("distances.csv", distances, delimiter =",",fmt ='% s')

# In[人口をくっつける]

with open("./distances.pickle", "rb") as f:
    distances = pickle.load(f)
pop = pd.read_csv("popdata_65.csv",encoding = "shift-jis")
df6 = pd.merge(pop, df1, on=['code'], how='inner')
df6.insert(1, 'distance', distances)


# In[表を作る]
import collections
from matplotlib.ticker import FormatStrFormatter
# sns.set(style="darkgrid", palette="muted", color_codes=True)
# sns.set(font="Yu Gothic",context="talk",style="white")

# x_idx = np.arange(df7.shape[0])
df7 = pd.DataFrame()
df7["distance"] = df6["distance"]
df7["H27_all"] = df6["H27_all"]

#距離と人口の関係性
df = pd.DataFrame()
for n in range(21):
    a = df7[df7.distance == n].H27_all.sum()
    b = pd.DataFrame([[n, a/100000]],columns=["label","value"])
    df = pd.concat([df, b], ignore_index =True)
    

# 「値」の降順にデータを並び替える
# df = df.sort_values(by="value", ascending=False)
# 累積和を求める
df["accum"] = np.cumsum(df["value"])
# 比率の累計を求める
df["accum_percent"] = df["accum"] / sum(df["value"]) * 100
 
# サイズ指定
fig = plt.figure(dpi=100, figsize=(12, 6))
# 軸関係の表示
ax = fig.add_subplot(111)
# データ数のカウント
data_num = len(df)
 
# 棒グラフの描画
ax.bar(range(data_num), df["value"], width=0.4, color="#3366ff", edgecolor="#0f1e4b", label="アクセス可能な人口")
ax.set_xticks(range(data_num))
ax.set_xticklabels(df["label"].tolist())
ax.set_xlabel("距離[100m]")
ax.set_ylabel("累計人口[100000人]")
ax.set_ylim([0, 6])
"""
# 折れ線グラフの描画
ax_add = ax.twinx()
ax_add.plot(range(data_num), df["accum_percent"], color="#ff8181", linewidth=2.5,
            marker="o",markersize=8, markeredgecolor="#000081", markeredgewidth=0.7,
            label="割合")
ax_add.set_ylim([0, 100])
ax_add.set_ylabel("割合[%]")
ax_add.spines['right'].set_color('#ff8181')
# 軸目盛りのフォーマット
ax_add.ｙaxis.set_major_formatter(FormatStrFormatter("%.1f"))
 """

# 折れ線グラフの描画2
ax_add2 = ax.twinx()
ax_add2.plot(range(data_num), df["accum"], color="blue", linewidth=2.5,
            marker="o",markersize=8, markeredgecolor="blue", markeredgewidth=0.7,
            label="累積")
ax_add2.set_ylim([0, 25])
ax_add2.set_ylabel("累積[1000000人]")
# ax_add2.spines['right'].set_color('blue')
# ax_add2.spines["right"].set_position(("axes", 1.2))
 

# 凡例
ax_handler, ax_label = ax.get_legend_handles_labels()
# ax_add_handler, ax_add_label= ax_add.get_legend_handles_labels()
ax_add2_handler, ax_add2_label= ax_add2.get_legend_handles_labels()
ax.legend(ax_handler  + ax_add2_handler, ax_label  + ax_add2_label, loc ='upper left',fontsize=15,ncol=1)
#+ ax_add_handler + ax_add_label

# 余白調整
plt.subplots_adjust(left=0.08, right=0.6, bottom=0.15, top=0.96)
 
# グラフを画像保存
plt.savefig("画像/result.png", facecolor="white")

# In[ジニだし１つ目]

def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d:
    # array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))

#Seriesのみでgini出せる
gini_result=pd.DataFrame(columns=["gini"])
ccc =pd.DataFrame(index=["病院の数H27_all"], columns=["gini"])
df = df.sort_values("value")
value_gini = df["value"]
ccc["gini"] =gini(value_gini)
gini_result = pd.concat([gini_result, ccc])



