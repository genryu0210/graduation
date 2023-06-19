import pandas as pd


csv_input = pd.read_csv(filepath_or_buffer="MESHDATA_01106.csv", encoding="ms932", sep=",")
for i in range(len(csv_input.index)):
    for n in range(len(csv_input.columns)):
        
        x=csv_input.iloc[i,n]
        if x == -9999 :
            csv_input.iloc[i,n]=0
        else:
            pass

csv_input.to_csv("aaa.csv", encoding = "shift-jis")
