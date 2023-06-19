# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:22:46 2021

@author: kenta
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
import pickle
from matplotlib.ticker import FormatStrFormatter

# In[]
df1 = pd.read_csv("clearpoint1.csv",encoding = "shift-jis")

with open("./sort_list.pickle", "rb") as f:
    x = pickle.load(f)
def gini(array):
    """Calculate the Gini coefficient of a numpy array."""

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
# In[]

gini_result=pd.DataFrame(columns=["gini"])
sum_result = pd.DataFrame(columns=["accesible_distance"])
pop = pd.read_csv("popdata_65.csv",encoding = "shift-jis")
df6 = pd.merge(pop, df1, on=['code'], how='inner')
name_list =["バス停の数", "公園の数", "駅の数", "病院の数", "スーパーの数"]
for l in range(len(name_list)):
    print(name_list[l])
    distances = list()
    for n in range(len(x)):
        dfx =x[n]
        # print(dfx.iloc[0,0])
        df5 = pd.merge(dfx, df1, left_on='search_code', right_on=['code'], how='inner')
        
        for i in range(len(df5)):
            if df5[name_list[l]][i] > 0:
                distances.append(df5["distanse_list"][i]) 
                # print(distances[n]) 
                break
            elif i == len(df5)-1 and df5[name_list[l]][i] == 0:
                distances.append(20) 
                # print(distances[n]) 
                break
            else:
                pass
    df6.insert(l+1, f'{name_list[l]}_distance', distances)
    
    sns.set(style="darkgrid", palette="muted", color_codes=True)
    sns.set(font="Yu Gothic",context="talk",style="white")
    pop_list =["H27_all", "H32_all", "H37_all", "H42_all", "H47_all", "H52_all", "H57_all", "H27_65", "H32_65", "H37_65", "H42_65", "H47_65", "H52_65", "H57_65"]
    for q in range(len(pop_list)):
        print(pop_list[q])
        df7 = pd.DataFrame()
        df7["distance"] = df6[f'{name_list[l]}_distance']
        df7["poplation"] = df6[pop_list[q]]
        df = pd.DataFrame()
        for n in range(21):
            a = df7[df7.distance == n].poplation.sum()
            b = pd.DataFrame([[n, a/100000]],columns=["label","value"])
            df = pd.concat([df, b], ignore_index =True)
        df8 =df
        # df = df.sort_values(by="value", ascending=False)
        df["accum"] = np.cumsum(df["value"])
        df["accum_percent"] = df["accum"] / sum(df["value"]) * 100
        fig = plt.figure(dpi=100, figsize=(12, 6))
        ax = fig.add_subplot(111)
        data_num = len(df)
        #棒グラフの描画
        ax.bar(range(data_num), df["value"], width=0.4, color="#3366ff", edgecolor="#0f1e4b", label="アクセス可能な人口")
        ax.set_xticks(range(data_num))
        ax.set_xticklabels(df["label"].tolist())
        ax.set_xlabel("距離[100m]")
        ax.set_ylabel("累計人口[100000人]")
        ax.set_ylim([0, 6])
        """
        #折れ線グラフの描画
        ax_add = ax.twinx()
        ax_add.plot(range(data_num), df["accum_percent"], color="#ff8181", linewidth=2.5,
                    marker="o",markersize=8, markeredgecolor="#000081", markeredgewidth=0.7,
                    label="割合")
        ax_add.set_ylim([0, 100])
        ax_add.set_ylabel("割合[%]")
        ax_add.spines['right'].set_color('#ff8181')
        ax_add.ｙaxis.set_major_formatter(FormatStrFormatter("%.1f"))
        """
        # 折れ線グラフの描画2
        ax_add2 = ax.twinx()
        ax_add2.plot(range(data_num), df["accum"], color="#ff8181", linewidth=2.5,
                    marker="o",markersize=8, markeredgecolor="#000081", markeredgewidth=0.7,
                    label="累積")
        ax_add2.set_ylim([0, 25])
        ax_add2.set_ylabel("累積[100000人]")
        # ax_add2.spines['right'].set_color('#ff8181')

        plt.subplots_adjust(left=0.08, right=0.6, bottom=0.15, top=0.96)
        
        # 凡例
        ax_handler, ax_label = ax.get_legend_handles_labels()
        # ax_add_handler, ax_add_label= ax_add.get_legend_handles_labels()
        ax_add2_handler, ax_add2_label= ax_add2.get_legend_handles_labels()
        ax.legend(ax_handler  + ax_add2_handler, ax_label  + ax_add2_label, loc ='upper left',fontsize=15,ncol=1)
        #+ ax_add_handler + ax_add_label
        
        plt.savefig(f'画像/{name_list[l]}_{pop_list[q]}.png', facecolor="white")
        """
        #Seriesのみでgini出せる

        ccc =pd.DataFrame(index=[f'{name_list[l]}_{pop_list[q]}'], columns=["gini"])
        df = df.sort_values("value")
        value_gini = df["value"]
        ccc["gini"] =gini(value_gini)
        gini_result = pd.concat([gini_result, ccc])
        #1人当たりのアクセス距離
        cccc =pd.DataFrame(index=[f'{name_list[l]}_{pop_list[q]}'], columns=["accesible_distance"])
        sum_list = df8["label"][0:20]*df8["value"][0:20]
        cccc["accesible_distance"] = sum(sum_list)/sum(df8["value"][0:20])
        sum_result = pd.concat([sum_result, cccc])
"""

# gini_sum = gini_result.join(sum_result)
df6.to_csv("result.csv", encoding='utf_8_sig')
# gini_sum.to_csv("gini_sum.csv", encoding='utf_8_sig')
