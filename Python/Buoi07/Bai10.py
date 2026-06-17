import re
doan_van = input("Nhap vao doan van: ")
so = re.findall(r'\b\w+\d\b', doan_van)
print(so)