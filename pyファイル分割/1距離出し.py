import pandas as pd
import pickle


csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")

result_list = []

test_columns = ["X_abs"]

for i in range(len(csv_input)):
    result = pd.DataFrame()
    for n in range(len(csv_input)):
        c = abs(csv_input["X"][i] - csv_input["X"][n])
        d = abs(csv_input["Y"][i] - csv_input["Y"][n])
        df1 = pd.DataFrame([[c, d, csv_input.loc[n, 'code'], 0, 0, 0]],columns=["X_abs", "Y_abs", "meshcode", "X_abs_m", "Y_abs_m", "distance"])
        result = pd.concat([result, df1], ignore_index = True)

    result_list.append(result)
    result.drop(range(0,len(csv_input),1), axis =0, )
print("1段階終わり")
for t in range(100):
    for u in range(100):
        
        result_list[t]["X_abs_m"][u] = result_list[t]["X_abs"][u] /0.00125*100 
        result_list[t]["Y_abs_m"][u] = result_list[t]["Y_abs"][u] /0.00083333*100 
        result_list[t]["X_abs_m"][u] = round(result_list[t]["X_abs_m"][u])
        result_list[t]["Y_abs_m"][u] = round(result_list[t]["Y_abs_m"][u])
        result_list[t]["distance"][u] = result_list[t]["X_abs_m"][u] + result_list[t]["Y_abs_m"][u]


with open("./data.pickle", "wb") as f:
    pickle.dump(result_list,f)


with open("./data.pickle", "rb") as f:
    x = pickle.load(f)