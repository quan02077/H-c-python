import json

def plus(line): a, b = [int(x) for x in line.split()]; return a + b
def minus(line): a, b = [int(x) for x in line.split()]; return a - b
def divide(line): a, b = [int(x) for x in line.split()]; return a / b
def multi(line): a, b = [int(x) for x in line.split()]; return a * b

data = ["18 2"]

try:
    with open("Bai05_data.txt", "w") as f:
        f.write("\n".join(data))
        print("Ghi thanh cong")

    with open("Bai05_data.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise ValueError("File khong co du lieu")
        
        results = []
        for line in lines:
            a, b = [int(x) for x in line.split()]
            results.append({
                "a": a,
                "b": b,
                "plus": plus(line),
                "minus": minus(line),
                "multi": multi(line),
                "divide": divide(line)
            })

        with open("Bai05_kq.json", "w") as f_output:
            json.dump(results, f_output, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("File khong ton tai")
except ValueError as e:
    print(f"Loi: {e}")
except Exception as ve:
    print(f"Loi khong xac dinh: {ve}")
