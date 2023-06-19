import pandas as pd

csv_input = pd.read_csv(filepath_or_buffer="近い公園.csv", encoding="ms932", sep=",")
popdata = pd.read_csv(filepath_or_buffer="popdata_all.csv", encoding="ms932", sep=",")



H27_65 = pd.DataFrame()
H27_65_seri = popdata["H27男65-69"] + popdata["H27男70-74"] + popdata["H27男75-79"] + popdata["H27男80-84"] + popdata["H27男85-"] + \
    popdata["H27女65-69"] + popdata["H27女70-74"] + popdata["H27女75-79"] + \
    popdata["H27女75-79"] + popdata["H27女80-84"] + popdata["H27女85-"]
H27_65["H27_65"] = pd.concat([H27_65, H27_65_seri])
H27_65 = H27_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H27_65)
popdata=popdata.reset_index()

H32_65 = pd.DataFrame()
H32_65_seri = popdata["H32男65-69"] + popdata["H32男70-74"] + popdata["H32男75-79"] + popdata["H32男80-84"] + popdata["H32男85-"] + \
    popdata["H32女65-69"] + popdata["H32女70-74"] + popdata["H32女75-79"] + \
    popdata["H32女75-79"] + popdata["H32女80-84"] + popdata["H32女85-"]
H32_65["H32_65"] = pd.concat([H32_65, H32_65_seri])
H32_65 = H32_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H32_65)
popdata=popdata.reset_index()

H37_65 = pd.DataFrame()
H37_65_seri = popdata["H37男65-69"] + popdata["H37男70-74"] + popdata["H37男75-79"] + popdata["H37男80-84"] + popdata["H37男85-"] + \
    popdata["H37女65-69"] + popdata["H37女70-74"] + popdata["H37女75-79"] + \
    popdata["H37女75-79"] + popdata["H37女80-84"] + popdata["H37女85-"]
H37_65["H37_65"] = pd.concat([H37_65, H37_65_seri])
H37_65 = H37_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H37_65)
popdata=popdata.reset_index()

H42_65 = pd.DataFrame()
H42_65_seri = popdata["H42男65-69"] + popdata["H42男70-74"] + popdata["H42男75-79"] + popdata["H42男80-84"] + popdata["H42男85-"] + \
    popdata["H42女65-69"] + popdata["H42女70-74"] + popdata["H42女75-79"] + \
    popdata["H42女75-79"] + popdata["H42女80-84"] + popdata["H42女85-"]
H42_65["H42_65"] = pd.concat([H42_65, H42_65_seri])
H42_65 = H42_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H42_65)
popdata=popdata.reset_index()

H47_65 = pd.DataFrame()
H47_65_seri = popdata["H47男65-69"] + popdata["H47男70-74"] + popdata["H47男75-79"] + popdata["H47男80-84"] + popdata["H47男85-"] + \
    popdata["H47女65-69"] + popdata["H47女70-74"] + popdata["H47女75-79"] + \
    popdata["H47女75-79"] + popdata["H47女80-84"] + popdata["H47女85-"]
H47_65["H47_65"] = pd.concat([H47_65, H47_65_seri])
H47_65 = H47_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H47_65)
popdata=popdata.reset_index()

H52_65 = pd.DataFrame()
H52_65_seri = popdata["H52男65-69"] + popdata["H52男70-74"] + popdata["H52男75-79"] + popdata["H52男80-84"] + popdata["H52男85-"] + \
    popdata["H52女65-69"] + popdata["H52女70-74"] + popdata["H52女75-79"] + \
    popdata["H52女75-79"] + popdata["H52女80-84"] + popdata["H52女85-"]
H52_65["H52_65"] = pd.concat([H52_65, H52_65_seri])
H52_65 = H52_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H52_65)
popdata=popdata.reset_index()

H57_65 = pd.DataFrame()
H57_65_seri = popdata["H57男65-69"] + popdata["H57男70-74"] + popdata["H57男75-79"] + popdata["H57男80-84"] + popdata["H57男85-"] + \
    popdata["H57女65-69"] + popdata["H57女70-74"] + popdata["H57女75-79"] + \
    popdata["H57女75-79"] + popdata["H57女80-84"] + popdata["H57女85-"]
H57_65["H57_65"] = pd.concat([H57_65, H57_65_seri])
H57_65 = H57_65.set_index(popdata["code"])
popdata = popdata.set_index("code")
popdata = popdata.join(H57_65)
popdata.to_csv("popdata_65.csv", encoding = "shift-jis")