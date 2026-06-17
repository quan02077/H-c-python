import re
doan_van = input("Nhap vao doan van: ")
co_so = re.findall(r'\d+\.?\d*', doan_van)
print(co_so)