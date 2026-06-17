import re
doan_van = input("Nhap vao doan van: ")
cau_tu = re.split(r'[.,!?]', doan_van)
cau_tu = [cau.strip() for cau in cau_tu if cau.strip()]
print(cau_tu)
