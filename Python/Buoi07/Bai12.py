import re
doan_van = input("Nhap vao doan van: ")
chu_in_hoa = re.findall(r'\b[A-Z]+\b', doan_van)
print(chu_in_hoa)