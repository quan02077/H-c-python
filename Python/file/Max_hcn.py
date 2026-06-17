import json

data = [
    {"width": 5, "height": 10},
    {"width": 7, "height": 3},
    {"width": 4, "height": 8},
    {"width": 6, "height": 6}
]

# Ghi file JSON
with open("hcn.json", "w") as file:
    json.dump(data, file)
    print("Ghi thanh cong")

def max_hcn(hcns):
    dt_max_hcn = None
    dt_max = 0
    for hcn in hcns:
        cd = hcn.get("width", 0)
        cr = hcn.get("height", 0)
        dt = cd * cr

        if dt > dt_max:
            dt_max = dt
            dt_max_hcn = hcn
    return dt_max_hcn

try: 
    with open("hcn.json", "r") as f:
        hcns = json.load(f)  

        max_Hcn = max_hcn(hcns)

        if max_Hcn:
            print(f"Chiều rộng của hình chữ nhật: {max_Hcn.get('width', 0)}")
            print(f"Chiều dài của hình chữ nhật: {max_Hcn.get('height', 0)}")
            print(f"Diện tích của hình chữ nhật: {max_Hcn.get('width', 0) * max_Hcn.get('height', 0)}")

        else:
            print("Không có hình chữ nhật nào trong dữ liệu")

except FileNotFoundError:
    print("File không tồn tại")
except json.JSONDecodeError:
    print("Không thể đọc dữ liệu JSON từ file")
except Exception as e:
    print(f"Lỗi khác: {e}")
