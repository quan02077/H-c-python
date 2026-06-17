import csv

data = [
    ['Tên', 'Tuổi', 'Địa chỉ'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'San Francisco'],
    ['Bob', '28', 'Los Angeles']
]

file_path = "test.csv"

with open(file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows(data)
    print(f"csv file '{file_path}' was created!")
with open(file_path, "r", encoding= "utf-8") as f:
    content = csv.reader(f)
    for line in content:
        print(line)