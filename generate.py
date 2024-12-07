import pandas as pd
import random

def generate_dataset(file_path):
    cities = ['Bishkek', 'Almaty', 'Moscow', 'London', 'Paris']
    vacation_preferences = ['Beach holiday', 'Cruise', 'Hiking', 'Shopping']
    transport_preferences = ['auto', 'plane', 'train']
    targets = ['Yes', 'No']

    # Генерация данных
    data = {
        'salary': [random.randint(20000, 100000) for _ in range(500)],
        'age': [random.randint(18, 65) for _ in range(500)],
        'city': [random.choice(cities) for _ in range(500)],
        'vacation_prefer': [random.choice(vacation_preferences) for _ in range(500)],
        'transport_prefer': [random.choice(transport_preferences) for _ in range(500)],
        'target': [random.choice(targets) for _ in range(500)],
    }

    df = pd.DataFrame(data)
    # Сохранение в Excel
    df.to_excel(file_path, index=False)
    print(f"Данные успешно сохранены в файл: {file_path}")

# Генерация базы данных
generate_dataset("vacation_preferences_dataset_generated.xlsx")
