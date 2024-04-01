import json
import csv
import os

# Hàm để đọc dữ liệu từ tệp JSON
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.loads(file.read())
    return data

# Hàm để ghi thông tin vào tệp CSV
def write_to_csv(data_list):
    csv_filename = 'info.csv'
    csv_exists = os.path.exists(csv_filename)

    # Ghi thông tin người dùng vào tệp CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not csv_exists:
            writer.writerow(['Name', 'Age', 'Education', 'Job', 'Hobby', 'ranking_list'])

        for data in data_list:
            writer.writerow([
                data['name'],
                data['info']['age'],
                data['info']['education'],
                data['info']['job'],
                data['info']['hobby'],
                data['ranking_list']
            ])

# Đọc dữ liệu từ tệp JSON
json_data = read_json_file('mess.json')

# Ghi thông tin vào tệp CSV
write_to_csv(json_data)  