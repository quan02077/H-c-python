import json
import csv 
import math

def loai_tam_giac(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Khong phai tam giac"
    if a == b == c:
        return "Deu"
    elif a == b or b == c or a == c:
        return "Can"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Vuong"
    else:
        return "Thuong"
    
def dien_tich(a, b, c):
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)

data = [
    {"a": 3, "b": 4, "c": 5},
    {"a": 5, "b": 5, "c": 5},
    {"a": 2, "b": 2, "c": 3},
    {"a": 10, "b": 2, "c": 3}
]
try:
    with open("tamgiac.json", "w") as f:
        json.dump(data, f)
        print("Ghi thanh cong")

    with open("tamgiac.json", "r") as f:
        lines = json.load(f)

        kq = []
        for line in lines:
            a, b, c = line["a"], line["b"], line["c"]
            loai = loai_tam_giac(a, b, c)
            if loai == "Khong phai tam giac":
                chuvi = dt = ""
            else:
                chuvi = a + b + c
                dt = dien_tich(a, b, c)
            kq.append([a, b, c, loai, chuvi, dt])

        with open("Bai06_kq.csv", "w") as f_output:
            write = csv.writer(f_output)
            write.writerow(["a", "b", "c", "Loai", "Chu vi", "Dien tich"])
            write.writerows(kq)
except FileNotFoundError:
    print("File khong ton tai")
except Exception as e:
    print("Loi:", e)