import pandas as pd
import random
from faker import Faker
import os
print("Current working directory:", os.getcwd())


# Initialize Faker for generating realistic data
fake = Faker()
Faker.seed(0)
random.seed(0)

# Generate 5000 unique records for CustomerInfo
data = {
    "ID": list(range(1, 5001)),
    "Name": [fake.unique.name() for _ in range(5000)],
    "Age": [random.randint(18, 75) for _ in range(5000)],
    "CustomerSince": [random.randint(2010, 2023) for _ in range(5000)],
    "HighestSpend": [random.randint(1000, 50000) for _ in range(5000)],
    "ZipCode": [random.randint(10000, 99999) for _ in range(5000)],
    "HiddenScore": [random.randint(300, 850) for _ in range(5000)],
    "MonthlyAverageSpend": [round(random.uniform(500.0, 10000.0), 2) for _ in range(5000)],
    "Level": [random.randint(1, 5) for _ in range(5000)],
    "Address": [fake.address().replace("\n", ", ") for _ in range(5000)],
    "Email": [fake.email() for _ in range(5000)],
    "Phone": [fake.phone_number() for _ in range(5000)],
    "DateOfBirth": [fake.date_of_birth(minimum_age=18, maximum_age=75) for _ in range(5000)],
    "AccountType": [random.choice(["Checking", "Savings", "Business"]) for _ in range(5000)],
    "Balance": [round(random.uniform(0.0, 50000.0), 2) for _ in range(5000)],
    "LoanAmount": [round(random.uniform(0.0, 30000.0), 2) for _ in range(5000)],
    "Income": [round(random.uniform(20000.0, 150000.0), 2) for _ in range(5000)]
}

# Create DataFrame
customer_info_df = pd.DataFrame(data)

# Save to CSV
customer_info_df.to_csv("CustomerInfo_Generated.csv", index=False)

print("CustomerInfo_Generated.csv has been created successfully!")
