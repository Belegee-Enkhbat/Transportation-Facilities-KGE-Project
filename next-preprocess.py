import pandas as pd

# Load the CSV file to understand its structure
file_path = 'transposed_output.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
data.head(), data.columns
# Rename columns from '0', '1', etc., to 'Bus Station 1', 'Bus Station 2', etc.
# We skip renaming 'Unnamed: 0' since it's likely a descriptive row

new_column_names = ['Attribute']  # This retains the original name for the first column
new_column_names.extend([f'Bus Station {i+1}' for i in range(len(data.columns) - 1)])

# Assign new column names
data.columns = new_column_names

# Save the updated DataFrame back to a CSV file
updated_file_path = 'transposed_output.csv'
data.to_csv(updated_file_path, index=False)

updated_file_path
