from faker import Faker  # This will now correctly import the Faker library
import pandas as pd

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1000

# Create a list to store the data
data = []

# Generate dummy data
for _ in range(num_records):
    record = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job": fake.job(),
        "company": fake.company(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'),
        "ssn": fake.ssn(),
        "credit_card_number": fake.credit_card_number(),
        "credit_card_expire": fake.credit_card_expire(),
        "city": fake.city(),
        "country": fake.country(),
        "latitude": fake.latitude(),
        "longitude": fake.longitude(),
        "text": fake.text(max_nb_chars=200),
    }
    data.append(record)

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("dummy_dataset.csv", index=False)

# Print the first few rows of the DataFrame
print(df.head())