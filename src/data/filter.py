import pandas as pd


def filter_lenght(data, col_1, col_2):
	data["col_1 lenght"] = data[col_1].apply(lambda sent : sent.split())
	data["col_2 lenght"] = data[col_2].apply(lambda sent : sent.split())


	data = data[data["col_1 lenght"].map(len) >= 6]
	data = data[data["col_2 lenght"].map(len) >= 6]

	return data[[col_1, col_2]]