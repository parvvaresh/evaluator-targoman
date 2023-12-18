import pandas as pd


def filter_lenght(data, columns, min_lenght):
    for col in columns:
        data = _filter_lenght(data, col, min_lenght)

    return data


def _filter_lenght(data, col, min_lenght):
    data["col lenght"] = data[col].apply(lambda sent: sent.split())

    data = data[data["col lenght"].map(len) >= min_lenght]
    data = data.drop(columns=["col lenght"])
    return data
