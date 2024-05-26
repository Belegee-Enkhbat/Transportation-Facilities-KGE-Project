import csv
from faker import Faker
import random
import os

# Create a Faker object
fake = Faker()

# Create a directory to store the CSV files if it doesn't exist
directory = 'Phase 4 - Knowledge Definition/data'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate and save 50 CSV files
for i in range(1, 2):
    # Generate random data
    data = [(j, fake.random_int(min=18, max=90), fake.random_element(["Male", "Female"]), fake.name(), fake.phone_number()) for j in range(1, 101)]

    # Write data to a CSV file
    filename = os.path.join(directory, f'passenger.csv')
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID', 'Age', 'Gender', 'Name', 'Phone Number'])
        csvwriter.writerows(data)

print("CSV files created successfully.")
