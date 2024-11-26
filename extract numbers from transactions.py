import pandas as pd
import re

# Load the Excel file (change 'file_path.xlsx' to your file's name and path)
file_path = r'C:\Users\yazam\OneDrive\Desktop\Files\Yazmin doc importantes\archivos\transactions.csv'
#sheet_name = 'transactions'  # specify the sheet name if needed
data = pd.read_csv(file_path)

# Specify the column name (for example, "Description")
columns_to_extract= ['amount', 'amount decimal']

# Define a function to extract numbers from a string
def extract_numbers(text):
    # Find all number sequences, including "-" if needed
    numbers = re.findall(r'-?\d+,\d+|-?\d+', str(text))
    return " ".join(numbers) if numbers else None

# Apply the function to each specified column and create a new column for each result
for col in columns_to_extract:
    data[f'Extracted_{col}'] = data[col].apply(extract_numbers)


# Apply the function to extract numbers in the specified column
data['Extracted_Numbers'] = data[columns_to_extract].apply(extract_numbers)

# Display the results (or save to a new file if needed)
print(data[['amount', 'Extracted_amount', 'amount decimal', 'Extracted_amount decimal']])
# Save to a new Excel file
data.to_csv("extracted_numbers.xlsx", index=False)