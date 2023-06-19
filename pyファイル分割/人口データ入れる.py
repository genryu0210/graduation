import pandas as pd


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")
pop1 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01101.csv", encoding="ms932", sep=",")
pop2 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01102.csv", encoding="ms932", sep=",")
pop3 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01103.csv", encoding="ms932", sep=",")
pop4 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01104.csv", encoding="ms932", sep=",")
pop5 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01105.csv", encoding="ms932", sep=",")
pop6 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01106.csv", encoding="ms932", sep=",")
pop7 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01107.csv", encoding="ms932", sep=",")
pop8 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01108.csv", encoding="ms932", sep=",")
pop9 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01109.csv", encoding="ms932", sep=",")
pop10 = pd.read_csv(filepath_or_buffer="人口データ/MESHDATA_01110.csv", encoding="ms932", sep=",")

meshcode_list = pd.DataFrame(index=csv_input["code"])
pop1= pop1.rename(columns={'MESHCODE': 'code'})
pop1 = pop1.set_index("code")
popdata1 = pd.merge(meshcode_list, pop1, on =["code", "code"], how= "inner")

pop2= pop2.rename(columns={'MESHCODE': 'code'})
pop2 = pop2.set_index("code")
popdata2 = pd.merge(meshcode_list, pop2, on =["code", "code"], how= "inner")

pop3= pop3.rename(columns={'MESHCODE': 'code'})
pop3 = pop3.set_index("code")
popdata3 = pd.merge(meshcode_list, pop3, on =["code", "code"], how= "inner")

pop4= pop4.rename(columns={'MESHCODE': 'code'})
pop4 = pop4.set_index("code")
popdata4 = pd.merge(meshcode_list, pop4, on =["code", "code"], how= "inner")

pop5= pop5.rename(columns={'MESHCODE': 'code'})
pop5 = pop5.set_index("code")
popdata5 = pd.merge(meshcode_list, pop5, on =["code", "code"], how= "inner")

pop6= pop6.rename(columns={'MESHCODE': 'code'})
pop6 = pop6.set_index("code")
popdata6 = pd.merge(meshcode_list, pop6, on =["code", "code"], how= "inner")

pop7= pop7.rename(columns={'MESHCODE': 'code'})
pop7 = pop7.set_index("code")
popdata7 = pd.merge(meshcode_list, pop7, on =["code", "code"], how= "inner")

pop8= pop8.rename(columns={'MESHCODE': 'code'})
pop8 = pop8.set_index("code")
popdata8= pd.merge(meshcode_list, pop8, on =["code", "code"], how= "inner")

pop9= pop9.rename(columns={'MESHCODE': 'code'})
pop9 = pop9.set_index("code")
popdata9 = pd.merge(meshcode_list, pop9, on =["code", "code"], how= "inner")

pop10= pop10.rename(columns={'MESHCODE': 'code'})
pop10= pop10.set_index("code")
popdata10 = pd.merge(meshcode_list, pop10, on =["code", "code"], how= "inner")

pop = pd.concat([pop1, pop2, pop3, pop4, pop5, pop6,pop7, pop8, pop9, pop10])
popdata = meshcode_list.join([pop])
popdata.to_csv("popdata_all.csv", encoding = "shift-jis")
