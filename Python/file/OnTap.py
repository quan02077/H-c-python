def read_int(line):
    try:
        number = [int(x.strip()) for x in line.split(",") if x.strip()]
        return number
    except ValueError:
        raise ValueError("Dong nay khong phai so nguyen")

def merge_and_sort(int1, int2):
    merge_list = int1 + int2
    merge_list.sort()
    return merge_list

data = [
    "124, 4234, 4234", 
    "2342, 5435, 342", 
]

with open("list.txt", "w") as f:
    f.writelines("\n".join(data))
    print("Ghi thanh cong")

try:
    with open("list.txt", "r") as f:
        lines = f.readlines()

        if len(lines) < 2:
            raise ValueError("File khong co du lieu")
        
        int1 = read_int(lines[0])
        int2 = read_int(lines[1])

        ds_sort = merge_and_sort(int1, int2)
        
        with open("result.txt", "w") as f_output:
            f_output.write(' '.join(map(str, ds_sort)))
except FileNotFoundError:
    print("Loi: File khong ton tai")
except ValueError as ve:
    print(f"Loi: {ve}")
except Exception as e:
    print(f"Loi khong xac dinh: {e}")
