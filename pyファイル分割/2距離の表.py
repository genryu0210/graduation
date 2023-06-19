import pandas as pd

csv_input = pd.read_csv(filepath_or_buffer="clearpoint.csv", encoding="ms932", sep=",")
result = pd.read_csv(filepath_or_buffer="result.csv", encoding="ms932", sep=",")

meshcode_list = csv_input["code"].tolist()







"""
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
    
    result1[meshcode_list[m]] = result_list[100*m:(100*m)+100]
    

result1.dtypes
result1.to_csv("distancetable.csv", encoding = "shift-jis")
"""