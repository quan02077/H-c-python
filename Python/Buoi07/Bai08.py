import re
doan_van = input("Nhap vao doan van: ")
dau_cau = re.findall(r'[.,!?;]', doan_van)
print(dau_cau)