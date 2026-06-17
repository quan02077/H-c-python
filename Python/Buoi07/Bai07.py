import re
doan_van = input("Nhap vao doan van: ")
tu_cu = input("Nhap vao tu can thay the: ")
tu_moi = input("Nhap vao tu moi de thay the tu cua: ")
doan_van_moi = re.sub(r'\b' + re.escape(tu_cu) + r'\b', tu_moi, doan_van, flags=re.IGNORECASE)
print(doan_van_moi)