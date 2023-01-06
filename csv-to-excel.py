import pandas as pd
import os

# Set the path to the folder containing the CSV files
csv_folder_path = '/path/to/csv/folder'

# Set the path to the folder where you want to save the Excel files
excel_folder_path = '/path/to/excel/folder'

# Loop through all the files in the CSV folder
for file in os.listdir(csv_folder_path):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
        # Read the CSV file using pandas
        df = pd.read_csv(os.path.join(csv_folder_path, file))
        # Convert the CSV file to an Excel file
        df.to_excel(os.path.join(excel_folder_path, file.replace('.csv', '.xlsx')), index=False)
