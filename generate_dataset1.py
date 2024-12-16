import csv
import random  # Import for generating random values
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the num ber of records to generate
num_records = 10000

# Define the output file name
output_file = "dataset1.csv"

# Generate dataset
data = [
    {
        "Country": fake.country(),
        "Age": fake.random_int(min=18, max=99),
        "Salary": fake.random_int(min=30, max=12098777755000), 
        "Purchased": random.choice(["yes", "no"]) ,
        "Email":fake.email()
    }
    for _ in range(num_records)
]

# Save to CSV file
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Country", "Age", "Salary", "Purchased","Email"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset with {num_records} records saved to {output_file}.")
