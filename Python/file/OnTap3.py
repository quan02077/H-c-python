import json
import csv

class Tai_Khoan:
    def __init__(self, soTK, tenKH, soDu):
        self.soTK = soTK
        self.tenKH = tenKH
        self.soDu = soDu
    def in_thong_tin(self):
        return {"SoTK": self.soTK, "TenKH": self.tenKH, "SoDu": self.soDu}
class QL_Tai_Khoan:
    def __init__(self, filename="tk.json", o_filename="tk.csv"):
        self.filename = filename
        self.o_filename = o_filename    
        self.tk = self.doc_file()
    def tao_file(self):
        data = [
                {"SoTK": "123", "TenKH": "Nguyen A", "SoDu": 5000000},
                {"SoTK": "456", "TenKH": "Tran B", "SoDu": 2000000}
                ]
        with open(self.filename, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.tk = [Tai_Khoan(p["SoTK"], p["TenKH"], p["SoDu"]) for p in data]
        print("Tao file thanh cong")
    def doc_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tk = [Tai_Khoan(p["SoTK"], p["TenKH"], p["SoDu"]) for p in data]
            print("Doc file thanh cong")
            return self.tk
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def luu_file(self):
        data = [p.in_thong_tin() for p in self.tk]
        with open(self.o_filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["SoTK", "TenKH", "SoDu"])
            writer.writeheader()
            writer.writerows(data)  
    def show_tk(self):
        if not self.tk:
            print("Danh sach rong")
            return 
        print("Danh sach tai khoan")
        for i, p in enumerate(self.tk, 1):
            print(f"{i}. So tai khoan: {p.soTK}, Ten khach hang: {p.tenKH}, So du: {p.soDu} VND")
    def them_tk(self):
        soTK = input("Nhap vao so tai khoan: ").strip()
        tenKH = input("Nhap vao ten khach hang: ").strip()
        try: 
            soDu = float(input("Nhap vao so du hien tai cua ban: "))
        except ValueError:
            print("So du phai la so")
            return
        self.tk.append(Tai_Khoan(soTK, tenKH, soDu))
        self.luu_file()
        print("Them tai khoan thanh cong")
    def nap_tien(self):
        self.show_tk()
        try:
            index = int(input("Nhập vào số thứ tự tài khoản muốn nạp tiền: ")) - 1
            if index < 0 or index >= len(self.tk):
                print("Tài khoản không tồn tại trong danh sách")
                return
            sotien_nap = float(input("Nhập vào số tiền cần nạp: "))
            if sotien_nap <= 0:
                print("Số tiền phải lớn hơn 0")
                return
            self.tk[index].soDu += sotien_nap  
            self.luu_file()                   
            print(f"Nạp tiền thành công! Số dư mới: {self.tk[index].soDu:.2f}")
        except ValueError:
            print("Lỗi nhập dữ liệu")
    def rut_tien(self):
        self.show_tk()
        try:
            index = int(input("Nhập vào số thứ tự tài khoản muốn rút tiền: ")) - 1
            if index < 0 or index >= len(self.tk):
                print("Tài khoản không tồn tại trong danh sách")
                return
            sotien_rut = float(input("Nhập vào số tiền cần rút: "))
            if sotien_rut <= 0:
                print("Số tiền phải lớn hơn 0")
                return
            if self.tk[index].soDu < sotien_rut:
                print("Số dư không đủ để rút tiền")
                return
            self.tk[index].soDu -= sotien_rut  
            self.luu_file()                   
            print(f"Rút tiền thành công! Số dư mới: {self.tk[index].soDu:.2f}")
        except ValueError:
            print("Lỗi nhập dữ liệu")

def menu():
    print("""
========== MENU ==========
1. Tạo file theo mẫu 
2. Hiển thị danh sách sinh viên
3. Thêm tài khoản mới
4. Nạp tiền
5. Rút tiền
6. Thoát
==========================
""")

def main():
    ql = QL_Tai_Khoan()
    while True:
        menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            ql.tao_file()
        elif lua_chon == "2":
            ql.show_tk()
        elif lua_chon == "3":
            ql.them_tk()
        elif lua_chon == "4":
            ql.nap_tien()
        elif lua_chon == "5":
            ql.rut_tien()
        elif lua_chon == "6":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
