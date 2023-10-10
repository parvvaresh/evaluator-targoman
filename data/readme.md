# Data Concatenation and Conversion Tool

This Python script is designed to help you concatenate multiple Excel files into a single CSV file and select specific columns from the input files. The primary use case for this script is to combine data from different sources for analysis or further processing.

## Requirements

- Python 3.x
- pandas library (you can install it using `pip install pandas`)

## Usage

1. Ensure you have all the Excel files you want to process in the same directory as this script.
2. Update the `list_dates` variable in the script with the names of your Excel files.
3. Run the script using a Python interpreter.

```bash
python data.py
```

4. The script will read the specified Excel files, concatenate them, and select specific columns (e.g., "refs-en" and "refs-fa").
5. The concatenated data will be saved as a CSV file named "data.csv" in the same directory as the script.

## Configuration

You can customize the script by modifying the following parts:

- `list_dates`: Add the names of your Excel files to this list.

## Example

Suppose you have the following Excel files in your directory:

- A-TEST.xlsx
- B-TEST.xlsx
- C-TEST.xlsx
- D-TEST.xlsx

Running the script with the provided configuration will create a CSV file named "data.csv" containing the columns "refs-en" and "refs-fa" from the concatenated data.

## Output

The script generates a CSV file named "data.csv" with the selected columns from the input Excel files. You can use this CSV file for further analysis or data processing.

Feel free to modify and adapt this script to your specific needs. If you have any questions or encounter issues, please don't hesitate to reach out for assistance.

