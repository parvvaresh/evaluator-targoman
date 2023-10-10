import pandas as pd

def data():
    list_dates=[
        "A-TEST.xlsx",
        "B-TEST.xlsx",
        "C-TEST.xlsx",
        "D-TEST.xlsx"
    ]
    dfs = []
    for data in list_dates:
        dfs.append(pd.read_excel(data))
    temp = pd.concat(dfs, axis=0)
    result = pd.DataFrame()
    result["refs-en"] = temp["Unnamed: 1"]
    result["refs-fa"] = temp["Unnamed: 2"]
    result.to_csv("data.csv")
    return result

print(data().head())