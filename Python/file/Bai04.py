import csv

def plus(line):
    a, b = [int(x) for x in line.split()]
    return a + b

def minus(line):
    a, b = [int(x) for x in line.split()]
    return a - b

def divide(line) :
    a, b = [int(x) for x in line.split()]
    return a / b

def multi(line):
    a, b = [int(x) for x in line.split()]
    return a * b

data = [
    "5 10",
    "24 6",
    "18 2",
    "120 3"
]
try:
    with open("so_nguyen.txt", "w") as f:
        f.writelines("\n".join(data))
        print("Ghi thanh cong")

    with open("so_nguyen.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("File khong du du lieu")
        
        with open("bai04_kq.csv", "w", ) as f_output:
            write = csv.writer(f_output)
            write.writerow(["A", "B", "A + B", "A - B", "A * B", "A / B"]) 
            for line in lines:
                a, b = [int(x) for x in line.split()]
                write.writerow([a, b, plus(line), minus(line), multi(line), divide(line)])
except FileNotFoundError:
    print("File khong ton tai")
except ValueError as e:
    print(f"Loi: {e}")
except Exception as ve:
    print(f"Loi khong xac dinh: {ve}")