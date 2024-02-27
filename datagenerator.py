import random
from faker import Faker
import json

fake = Faker()

def create_data_entry():
    return {
        "end_year": random.randint(2020, 2030) if random.choice([True, False]) else None,
        "intensity": random.randint(1, 10),
        "sector": random.choice(["Energy", "Environment", "Manufacturing", "Financial services"]),
        "topic": random.choice(["AI", "COVID-19", "Blockchain", "Renewable Energy", "Online Learning"]),
        "insight": fake.sentence(nb_words=6),
        "url": fake.url(),
        "region": random.choice(["North America", "Europe", "Asia", "South America", "Africa"]),
        "start_year": random.randint(2010, 2020),
        "impact": random.randint(1, 10),
        "added": fake.date_time_between(start_date="-3y", end_date="now").isoformat(),
        "published": fake.date_time_between(start_date="-3y", end_date="now").isoformat(),
        "country": fake.country(),
        "relevance": random.randint(1, 10),
        "pestle": random.choice(["Technological", "Health", "Economic", "Environmental", "Political"]),
        "source": fake.company(),
        "title": fake.sentence(nb_words=4),
        "likelihood": random.randint(1, 10)
    }

def generate_dataset(num_entries=500):
    return [create_data_entry() for _ in range(num_entries)]

# Generate the dataset
dataset = generate_dataset(500)

# Print the dataset to console or write it to a file
# print(json.dumps(dataset, indent=2))

# Writing to a JSON file
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)
