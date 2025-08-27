import pandas as pd

# Load the Excel file
excel_file = 'C:/Users/shiva/Desktop/ss/May2231.xlsx'

# Initialize an empty DataFrame to hold all data
merged_df = pd.DataFrame()

# Iterate through each sheet in the Excel file
for sheet_name in pd.ExcelFile(excel_file).sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Append the data to the merged DataFrame
    merged_df = pd.concat([merged_df, df])

# Save the merged DataFrame to a new sheet in a new Excel file
merged_df.to_excel('C:/Users/shiva/Desktop/ss/May2231.xlsx', index=False)

print("Sheets merged into one successfully in merged_output.xlsx")
