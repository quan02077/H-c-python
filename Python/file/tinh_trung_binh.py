def trung_binh(numbers):
    tong = sum(numbers)
    return tong / len(numbers)

data = [
    "124, 4234, 4234", 
    "2342, 5435, 342", 
    "756, 254, 363"
]
with open("so.txt", "w") as f:
    f.writelines('\n'.join(data))
    print("Them thanh cong")
 
try:
    with open("so.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("File khong co du lieu")
        
        with open("kq.txt", "w") as f_output:
            for line in lines:
                for num in line.split():
                    numbers = [int(x.strip()) for x in line.split(",") if x.strip()]
                avg = trung_binh(numbers)
                f_output.write(f"{avg}\n")
except FileNotFoundError:
    print("Loi: File khong ton tai")
except ValueError as ve:
    print(f"Loi: {ve}")
except Exception as e:
    print(f"Loi khong xac dinh: {e}")

