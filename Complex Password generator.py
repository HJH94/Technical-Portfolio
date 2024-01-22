import pandas as pd
import random

# Specify the path to your Excel file
excel_file_path = r"C:\Users\harry\Documents\GitHub\Technical-Portfolio\Password Prompts.xlsx"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Get a random row index
random_row_index = random.randint(0, len(df) - 1)

# Get values from random cells in columns A and B
random_cell_A = df.loc[random_row_index, 'A']
random_cell_B = df.loc[random_row_index, 'B']

# Generate a random 4-digit code
random_code = random.randint(1000, 9999)

# Combine values from columns A and B with the random code
result = f"{random_cell_A}_{random_cell_B}_{random_code}"

# Print the result
print("Result:", result)
