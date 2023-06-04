import csv

def categorize_csv(filename, category_column):
    categories = {}

    with open(filename, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row[category_column]

            if category not in categories:
                categories[category] = []

            categories[category].append(row)

    return categories

filename = 'megaGymDataset.csv'
category_column = 'Level'

result = categorize_csv(filename, category_column)

for category, rows in result.items():
    print(f"Category: {category}")
    for i in range(len(result[category])):
        print(result[category][i]['Title'])
    print()
