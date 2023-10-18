# DataFrame Length Filter

This Python script is designed to filter a DataFrame based on the length of values in specified columns. It uses the `pandas` library to perform the filtering operation. The primary use case is to retain rows in the DataFrame where the values in specific columns have a length of at least 6.

## Usage

1. Make sure you have the `pandas` library installed. You can install it using `pip`:

   ```
   pip install pandas
   ```

2. Define your DataFrame, and specify the columns you want to filter. The script is designed to work with two columns, "col_1" and "col_2," but you can customize it for your specific DataFrame and column names.

3. Use the `filter_length` function to filter the DataFrame. Here's an example of how to use it:

   ```python
   filtered_data = filter_length(data, col_1="column_name_1", col_2="column_name_2")
   ```

   - The `data` parameter is your DataFrame.
   - The `col_1` parameter is the name of the first column you want to filter.
   - The `col_2` parameter is the name of the second column you want to filter.

4. The function will add two new columns to your DataFrame, "col_1 length" and "col_2 length," containing the length of the values in those columns.

5. Rows where the lengths of both columns are less than 6 will be removed from the DataFrame.

6. The filtered DataFrame, containing only rows where both "col_1" and "col_2" have lengths of at least 6, will be returned.

## Example

Here's an example of how to use the function to filter a DataFrame:

```python
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    "col_1": ["This is a long sentence", "Short", "Another example"],
    "col_2": ["A short one", "Longer sentence with more words", "Just a few words"]
})

filtered_data = filter_length(data, col_1="col_1", col_2="col_2")
print(filtered_data)
```

The resulting `filtered_data` DataFrame will only contain the rows where both "col_1" and "col_2" have lengths of at least 6 characters.

## Disclaimer

This script is a simple utility for DataFrame filtering and can be adapted to your specific data and column names. You may need to modify the column names or other aspects of the code to fit your requirements.

---

# Get File Path Utility

This Python script provides a simple utility function to obtain the path of a file located in the same directory as the script. The primary use case is to retrieve the path to a file named "data.csv," which is assumed to be in the same directory as the script. The script uses the `os` library to achieve this.

## Usage

1. Make sure you have the `os` library available, which is a built-in library in Python.

2. Use the `get_path` function to obtain the file path. Here's an example of how to use it:

   ```python
   file_path = get_path()
   print(file_path)
   ```

   The function will return the path to the "data.csv" file in the same directory as the script.

## Example

Here's an example of how to use the function to get the path to the "data.csv" file:

```python
import os

def get_path():
    return os.path.dirname(__file__) + "/data.csv"

file_path = get_path()
print("Path to data.csv:", file_path)
```

The `file_path` variable will contain the full path to the "data.csv" file in the same directory as the script.

## Disclaimer

This script is a simple utility for obtaining the path to a file in the same directory as the script. You may need to modify the file name or directory path as needed for your specific use case.

## License

This code is provided as-is and is open-source. You can use, modify, and distribute it according to your needs. Make sure to respect the licenses and terms of any third-party libraries you use in conjunction with this script.

---

Feel free to customize the README according to your project's specific needs and requirements.



