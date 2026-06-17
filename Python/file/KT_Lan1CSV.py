import csv

class San_Pham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia
    def in_thong_tin(self):
        return {"Ten": self.ten, "Gia": self.gia}

class QL_San_Pham:
    def __init__(self, filename="product.csv"):
        self.filename = filename
        self.product = self.doc_csv()

    def tao_csv(self):
        data = [
            {"Ten": "Áo thun", "Gia": 120000},
            {"Ten": "Giày thể thao", "Gia": 550000}
        ]
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Ten", "Gia"])
            writer.writeheader()
            writer.writerows(data)
        print("Tạo file CSV thành công")

    def doc_csv(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [San_Pham(row["Ten"], float(row["Gia"])) for row in reader]
        except FileNotFoundError:
            return []
        except Exception:
            return []

    def luu_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Ten", "Gia"])
            writer.writeheader()
            for p in self.product:
                writer.writerow(p.in_thong_tin())

    def show_san_pham(self):
        if not self.product:
            print("Danh sách rỗng")
            return
        print("Danh sách sản phẩm:")
        for i, p in enumerate(self.product, 1):
            print(f"{i}. {p.ten} - Giá: {p.gia} VND")

    def them_SP(self):
        ten = input("Nhập tên sản phẩm: ").strip()
        try:
            gia = float(input("Nhập giá sản phẩm: "))
        except ValueError:
            print("Giá phải là số!")
            return
        self.product.append(San_Pham(ten, gia))
        self.luu_csv()
        print("Thêm sản phẩm thành công!")

    def update_SP(self):
        self.show_san_pham()
        try:
            index = int(input("Nhập số thứ tự sản phẩm cần sửa: ")) - 1
            if index < 0 or index >= len(self.product):
                print("Sản phẩm không tồn tại!")
                return
            ten = input("Nhập tên sản phẩm mới: ").strip()
            gia = float(input("Nhập giá sản phẩm mới: "))
            self.product[index].ten = ten
            self.product[index].gia = gia
            self.luu_csv()
            print("Cập nhật sản phẩm thành công!")
        except ValueError:
            print("Lỗi nhập dữ liệu!")

    def xoa_SP(self):
        self.show_san_pham()
        try:
            index = int(input("Nhập số thứ tự sản phẩm cần xóa: ")) - 1
            if index < 0 or index >= len(self.product):
                print("Sản phẩm không tồn tại!")
                return
            del self.product[index]
            self.luu_csv()
            print("Xóa sản phẩm thành công!")
        except ValueError:
            print("Lỗi nhập dữ liệu!")

    def tong_tien(self):
        tong = sum(p.gia for p in self.product)
        print(f"Tổng giá trị các sản phẩm: {tong} VND")

    def max_min_gia(self):
        if not self.product:
            print("Danh sách rỗng.")
            return
        Max = max(self.product, key=lambda p: p.gia)
        Min = min(self.product, key=lambda p: p.gia)
        print(f"Sản phẩm giá cao nhất: {Max.ten} - {Max.gia} VND")
        print(f"Sản phẩm giá thấp nhất: {Min.ten} - {Min.gia} VND")


def menu():
    print("""
========== MENU ==========
1. Tạo file theo mẫu
2. Hiển thị danh sách sản phẩm
3. Thêm sản phẩm mới
4. Cập nhật sản phẩm
5. Xóa sản phẩm
6. Tính tổng giá trị sản phẩm
7. Tìm sản phẩm có giá cao nhất và thấp nhất
8. Thoát
==========================
""")


def main():
    ql = QL_San_Pham()
    while True:
        menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            ql.tao_csv()
        elif lua_chon == "2":
            ql.show_san_pham()
        elif lua_chon == "3":
            ql.them_SP()
        elif lua_chon == "4":
            ql.update_SP()
        elif lua_chon == "5":
            ql.xoa_SP()
        elif lua_chon == "6":
            ql.tong_tien()
        elif lua_chon == "7":
            ql.max_min_gia()
        elif lua_chon == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
