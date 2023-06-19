
import pandas as pd


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")

test_columns = ["X_abs"]
result = pd.DataFrame(columns=test_columns)
for i in range(len(csv_input)):
    for n in range(len(csv_input)):
        a = i
        b = n
        c = abs(csv_input["X"][a] - csv_input["X"][b])
        d = abs(csv_input["Y"][a] - csv_input["Y"][b])
        df1 = pd.DataFrame([[c, d, csv_input.loc[n, 'code'], csv_input.loc[i, "code"]]],columns=["X_abs", "Y_abs", "meshcode", "code"])
        result = pd.concat([result, df1])
        
result["X_abs_m"] = result["X_abs"] /0.00125*100 
result["Y_abs_m"] = result["Y_abs"] /0.00083333*100 
result["X_abs_m"] = round(result["X_abs_m"])
result["Y_abs_m"] = round(result["Y_abs_m"])

result["distance"] = result["X_abs_m"] + result["Y_abs_m"]
result.index = result["code"]
result.to_csv("result.csv")


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")
result = pd.read_csv(filepath_or_buffer="result.csv", encoding="ms932", sep=",")

merged_result = pd.merge(csv_input, result)

result1 = pd.DataFrame(index = merged_result["code"], columns = merged_result["meshcode"])
# codeをindexから解除
result1 = result1.reset_index()
# codeの被りを消す
result1 = result1.drop_duplicates()
meshcode_list= result1["code"].tolist()
result1 = result1.set_index("code")
result1 = result1.T

# codeをindexから解除
result1 = result1.reset_index()
# codeの被りを消す
result1 = result1.drop_duplicates()
result1 = result1.set_index("meshcode")
result_list = result["distance"].tolist()

for m in range(len(meshcode_list)):
    
    result1[meshcode_list[m]] = result_list[33681*m:(33681*m)+33681]
    

result1.dtypes
result1.to_csv("distancetable.csv", encoding = "shift-jis")


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")
distancetable = pd.read_csv(filepath_or_buffer="distancetable.csv", encoding="ms932", sep=",")


distancetable["meshcode"] = distancetable["meshcode"].astype("int64")
distancetable["meshcode"] = distancetable["meshcode"].astype("str")
meshcode_list= distancetable["meshcode"].tolist()

distancetable = distancetable.set_index("meshcode")
dont_sort = distancetable
nearst_park = pd.DataFrame()
for i in range(len(meshcode_list)):
    distancetable = distancetable.sort_values(by=meshcode_list[i]) 
    for n in range(len(meshcode_list)):
        if csv_input["公園の数"][n] > 0:
                    distance_m = dont_sort.iloc[n, i]
                    
                    if nearst_park.empty ==True :
                        df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                        nearst_park = pd.concat([nearst_park, df2]) 
                    else:
                        pass                      
                    
                    if nearst_park["meshcode_s"][len(nearst_park)-1] == meshcode_list[i]:
                        
                        if nearst_park["distance"][len(nearst_park)-1] == distance_m :
                            df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                            nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                        elif nearst_park["distance"][len(nearst_park)-1] > distance_m :
                                df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                                nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                                nearst_park = nearst_park.drop(nearst_park.index[[len(nearst_park)-2]])
                                nearst_park = nearst_park.reset_index(drop = True)
                        else:
                            pass
                    elif nearst_park["meshcode_s"][len(nearst_park)-1] != meshcode_list[i]:
                        df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                        nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                    else:
                        pass
                    

        else:
            pass

nearst_park.to_csv("近い公園.csv", encoding = "shift-jis")


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")
distancetable = pd.read_csv(filepath_or_buffer="distancetable.csv", encoding="ms932", sep=",")


distancetable["meshcode"] = distancetable["meshcode"].astype("int64")
distancetable["meshcode"] = distancetable["meshcode"].astype("str")
meshcode_list= distancetable["meshcode"].tolist()

distancetable = distancetable.set_index("meshcode")
dont_sort = distancetable
nearst_park = pd.DataFrame()
for i in range(len(meshcode_list)):
    distancetable = distancetable.sort_values(by=meshcode_list[i]) 
    for n in range(len(meshcode_list)):
        if csv_input["公園の数"][n] > 0:
                    distance_m = dont_sort.iloc[n, i]
                    
                    if nearst_park.empty ==True :
                        df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                        nearst_park = pd.concat([nearst_park, df2]) 
                    else:
                        pass                      
                    
                    if nearst_park["meshcode_s"][len(nearst_park)-1] == meshcode_list[i]:
                        
                        if nearst_park["distance"][len(nearst_park)-1] == distance_m :
                            df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                            nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                        elif nearst_park["distance"][len(nearst_park)-1] > distance_m :
                                df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                                nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                                nearst_park = nearst_park.drop(nearst_park.index[[len(nearst_park)-2]])
                                nearst_park = nearst_park.reset_index(drop = True)
                        else:
                            pass
                    elif nearst_park["meshcode_s"][len(nearst_park)-1] != meshcode_list[i]:
                        df2 = pd.DataFrame([[meshcode_list[i], distance_m, meshcode_list[n]]],columns=["meshcode_s", "distance", "meshcode_f"])
                        nearst_park = pd.concat([nearst_park, df2], ignore_index = True)
                    else:
                        pass
                    

        else:
            pass

nearst_park.to_csv("近い公園.csv", encoding = "shift-jis")
