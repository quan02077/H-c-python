def total(numbers):
    tong = sum(numbers)
    return tong

data =[
    "124 4234 4234", 
    "234 5435 342", 
    "756 254 363"
]
try:
    with open("tong.txt", "w") as f:
        f.writelines("\n".join(data))
        print("Ghi thanh cong")

    with open("tong.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("File khong co du lieu")
        
        with open("ket_qua.txt", "w") as f_output:
            for line in lines:
                for num in line:
                    numbers = [int(x.strip()) for x in line.split() if x.strip()]
                t = total(numbers)
                f_output.write(f"{t}\n")

except FileNotFoundError:
    print("File khon ton tai")
except ValueError as ve:
    print(f"Loi: {ve}")
except Exception as e:
    print(f"Loi khong xac dinh: {e}")