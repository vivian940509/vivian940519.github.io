import csv
import json

# 讀取 CSV 檔案
csv_file_path = 'csvReport.csv'
json_file_path = 'csvReport.json'

data = []

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 寫入 JSON 檔案
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"CSV 檔案已成功轉換為 JSON 檔案，並儲存在 {json_file_path}")