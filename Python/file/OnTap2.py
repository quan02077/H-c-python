import json

class Sinh_Vien:
    def __init__(self, ten, tuoi, lop, diem_tb):
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop
        self.diem_tb = diem_tb
    def in_thong_tin(self):
        return {
        "Ten": self.ten,
        "Tuoi": self.tuoi,
        "Lop": self.lop,
        "DiemTB": self.diem_tb
        }
class QL_SinhVien:
    def __init__(self, filename = "sinhvien.json"):
        self.filename = filename
        self.sv = self.doc_file()
    def tao_file(self):
        data = [
                {"Ten": "Minh", "Tuoi": 18, "Lop": "12A1", "DiemTB": 8.2},
                {"Ten": "Lan", "Tuoi": 17, "Lop": "12A2", "DiemTB": 9.0}
                ]
        with open(self.filename, "w", encoding= "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.sv = [Sinh_Vien(p["Ten"], p["Tuoi"], p["Lop"], p["DiemTB"]) for p in data]
        print("Tao file thanh cong")
    def doc_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.sv = [
                    Sinh_Vien(
                        p.get("Ten", ""),
                        p.get("Tuoi", 0),
                        p.get("Lop", ""),
                        p.get("DiemTB", 0)
                    )
                    for p in data
                ]
            return self.sv
        except (FileNotFoundError, json.JSONDecodeError):
            print("File bị lỗi hoặc không tồn tại")
            return []
    def luu_file(self):
        data = [p.in_thong_tin() for p in self.sv]
        with open(self.filename, "w", encoding= "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    def show_sv(self):
        if not self.sv:
            print("Danh sach rong")
            return 
        print("Danh sach sinh vien")
        for i, p in enumerate(self.sv, 1):
            print(f"{i}. Ten: {p.ten}, Tuoi: {p.tuoi}, Lop: {p.lop}, Diem trung binh: {p.diem_tb}")
    def them_sv(self):
        ten = input("Nhap vao ten sinh vien: ").strip()
        lop = input("Nhap vao lop sinh vien: ").strip()
        try:
            tuoi = int(input("Nhap vao tuoi sinh vien: "))
            diem_tb = float(input("Nhap vap diem trung binh sinh vien: "))
        except ValueError:
            print("Tuoi va diem trung binh phai la so")
            return
        self.sv.append(Sinh_Vien(ten, tuoi, lop, diem_tb))
        self.luu_file()
        print("Them sinh vien thanh cong")
    def cap_nhap_sv(self):
        self.show_sv()
        try:
            index = int(input("Nhập vào số thứ tự của sinh viên cần cập nhật/xóa: ")) - 1
            if index < 0 or index >= len(self.sv):
                print("Sinh vien khong ton tai trong danh sach")
                return
            ten = input("Nhap vao ten sinh vien: ").strip()
            tuoi = int(input("Nhap vao tuoi sinh vien: "))
            lop = input("Nhap vao lop sinh vien: ").strip()
            diem_tb = float(input("Nhap vap diem trung binh sinh vien: "))
            self.sv[index].ten = ten
            self.sv[index].tuoi = tuoi
            self.sv[index].lop = lop
            self.sv[index].diem_tb = diem_tb
            self.luu_file()
            print("Cap nhat sinh vien thanh cong")
        except ValueError:
            print("Loi nhap du lieu")
        def xoa_sv(self):
            self.show_sv()
            try:
                index = int(input("Nhập vào số thứ tự của sinh viên cần cập nhật/xóa: ")) - 1
                if index < 0 or index >= len(self.sv):
                    print("Sinh vien khong ton tai trong danh sach")
                    return
                del self.sv[index]
                self.luu_file()
                print("Xoa sinh vien thanh cong")
            except ValueError:
                print("Loi nhap du lieu")
    def diem_trung_binh_lop(self):
        if not self.sv:
            print("Danh sách rỗng, không thể tính điểm trung bình")
            return
        tong = sum(p.diem_tb for p in self.sv)
        tb = tong / len(self.sv)
        print(f"Diem trung binh cua lop: {tb:.2f}")
    def max_min_diem_tb(self):
        if not self.sv:
            print("Danh sach rong")
            return 
        Max = max(self.sv, key= lambda p:p.diem_tb)
        Min = min(self.sv, key= lambda p:p.diem_tb)
        print(f"Diem trung binh cao nhat: {Max.ten} - {Max.tuoi} - {Max.lop} - {Max.diem_tb}")
        print(f"Diem trung binh thap nhat: {Min.ten} - {Min.tuoi} - {Min.lop} - {Min.diem_tb}")


def menu():
    print("""
========== MENU ==========
1. Tạo file theo mẫu 
2. Hiển thị danh sách sinh viên
3. Thêm sinh viên mới
4. Cập nhật sinh viên
5. Xóa sinh viên
6. Tính điểm trung binh toàn lớp
7. Tìm sinh viên có điểm trung bình cao nhất và thấp nhất
8. Thoát
==========================
""")
    
def main():
    sv = QL_SinhVien()
    while True:
        menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            sv.tao_file()
        elif lua_chon == "2":
            sv.show_sv()
        elif lua_chon == "3":
            sv.them_sv()
        elif lua_chon == "4":
            sv.cap_nhap_sv()
        elif lua_chon == "5":
            sv.xoa_sv()
        elif lua_chon == "6":
            sv.diem_trung_binh_lop()
        elif lua_chon == "7":
            sv.max_min_diem_tb()
        elif lua_chon == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()