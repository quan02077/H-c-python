def count_tu(line):
    tu = line.split()
    return len(tu)

data = [
    "Hom nay tui vui vai chuong",
    "Today i was so happy",
    "Visca Barca"
]
try:
    with open("dem_tu.txt", "w") as f:
        f.writelines("\n".join(data))
        print("Ghi thanh cong")

    with open("dem_tu.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("File khong co du lieu")
        
        with open("sau_khi dem.txt", "w") as f_output:
            for line in lines:
                cnt = count_tu(line)
                f_output.write(f"{cnt}\n")
except FileNotFoundError:
    print("File khong ton tai")
except ValueError as e:
    print(f"Loi: {e}")
except Exception as ve:
    print(f"Loi khong xac dinh: {ve}")