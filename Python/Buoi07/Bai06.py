import re
doan_van = input("Nhap vao doan van: ")
tu_chua_a = re.findall(r'\b\w*a\w*\b', doan_van, flags = re.IGNORECASE)
print(tu_chua_a)