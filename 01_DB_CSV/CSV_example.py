import csv


def analise_sales(file_path):
    total_revenue = 0
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print(reader)
        for row in reader:
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_revenue += quantity * price
            data.append(row)
    return total_revenue, data


if __name__ == '__main__':
    revenue, my_data = analise_sales(r'files\sales.csv')
    print(revenue)
    print(my_data)
