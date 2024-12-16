import csv
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the number of records to generate
num_records = 10000

# Define the output file name
output_file = "dataset.csv"

# Generate dataset
data = [
    {
        "Name": fake.name(),
        "Email": fake.email(),
        "Address": fake.address().replace("\n", ", "),
        "Age": fake.random_int(min=18, max=99)
    }
    for _ in range(num_records)
]

# Save to CSV file
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Address", "Age"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset with {num_records} records saved to {output_file}.")
