import pandas as pd

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
