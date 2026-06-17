import json

class San_Pham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def in_thong_tin(self):
        return {"Ten": self.ten, "Gia": self.gia}


class QL_San_Pham:
    def __init__(self, filename="product.json"):
        self.filename = filename
        self.product = self.doc_json()

    def tao_json(self):
        data = [
            {"Ten": "Áo thun", "Gia": 120000},
            {"Ten": "Giày thể thao", "Gia": 550000}
        ]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Tạo file thành công.")

    def doc_json(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                du_lieu = json.load(f)
                return [San_Pham(p["Ten"], p["Gia"]) for p in du_lieu]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def luu_json(self):
        data = [p.in_thong_tin() for p in self.product]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def show_san_pham(self):
        if not self.product:
            print("Danh sách rỗng.")
            return
        print("\nDanh sách sản phẩm:")
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
        self.luu_json()
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
            self.luu_json()
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
            self.luu_json()
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
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tính tổng giá trị sản phẩm
6. Tìm sản phẩm có giá cao nhất và thấp nhất
7. Thoát
==========================
""")


def main():
    ql = QL_San_Pham()
    while True:
        menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            ql.show_san_pham()
        elif lua_chon == "2":
            ql.them_SP()
        elif lua_chon == "3":
            ql.update_SP()
        elif lua_chon == "4":
            ql.xoa_SP()
        elif lua_chon == "5":
            ql.tong_tien()
        elif lua_chon == "6":
            ql.max_min_gia()
        elif lua_chon == "7":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
