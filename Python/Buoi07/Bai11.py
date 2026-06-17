import re
doan_van = input("Nhap vao doan van: ")
do_dai_bang_5 = re.findall(r'\b\w{5}\b',doan_van)
print(do_dai_bang_5)