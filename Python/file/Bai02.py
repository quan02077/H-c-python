def reverse(line):
    dao_nguoc = line[::-1]
    return dao_nguoc

data = [
    "Hom nay tui vui vai chuong",
    "Today i was so happy",
    "Visca Barca"
]
try:
    with open("chuoi.txt", "w") as f:
        f.writelines("\n".join(data))
        print("Ghi thanh cong")

    with open("chuoi.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("File khong co du lieu")
        
        with open("reversed.txt", "w") as f_output:
            for line in lines:
                rev = reverse(line)
                f_output.write(f"{rev}\n")
except FileNotFoundError:
    print("File khong ton tai")
except ValueError as e:
    print(f"Loi: {e}")
except Exception as ve:
    print(f"Loi khong xac dinh: {ve}")