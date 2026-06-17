import re
doan_van = input("Nhap vao doan van: ")
in_hoa = re.findall(r'\b[A-Z]\w*', doan_van)
print(in_hoa)