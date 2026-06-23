import csv
import os

INPUT_DIR = './data'
OUTPUT_FILE = 'formatted_sales_data.csv'
TARGET_PRODUCT = 'pink morsel'

def process_data():
    formatted_data = [['Sales', 'Date', 'Region']]
    
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.csv'):
            file_path = os.path.join(INPUT_DIR, filename)
            
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    if row['product'].strip().lower() == TARGET_PRODUCT:
                        price = float(row['price'].replace('$', ''))
                        quantity = int(row['quantity'])
                        sales = price * quantity
                        
                        formatted_data.append([sales, row['date'], row['region']])
                        
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(formatted_data)

if __name__ == '__main__':
    process_data()