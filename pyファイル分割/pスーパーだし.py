# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:20:09 2021

@author: kenta
"""


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

supermarket = pd.read_csv(filepath_or_buffer="combined.csv", encoding="ms932", sep=",")
my_list = supermarket.sort_values(by="物販（食品）件数", ascending=False)

# In[]
super_df = pd.DataFrame()
# f'{name_list[l]}_{pop_list[q]}'
name_list =["スーパーアークス", "イオンモール", "業務スーパー", "コープさっぽろ", "薄野市場", "西友", "全日食チェーン", "東光ストア", "フードセンター", "北海市場", "まいばすけっと", "マックスバリュ", "ラルズマート", "イオン札幌", "イオンショッピングセンター", "イトーヨーカドー", "卸売スーパー", "ザ・ビッグエクスプレス", "生鮮市場", "メガセンタートライアル", "ホクレンショップ", "ビッグハウス", "マルコストアー", "ホクノースーパー", "産直"]
for i in range(len(name_list)):
    s  = my_list[my_list['建物名'].str.contains(name_list[i],  na=False)]
    super_df = pd.concat([super_df, s])

super_df.to_csv("スーパーマーケット.csv", encoding='utf_8_sig')