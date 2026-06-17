import re
doan_van = input("Nhap vao doan van: ")
tach_tu = re.findall(r'\w+', doan_van)
print(tach_tu)