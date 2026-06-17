import json
from datetime import datetime, date 

class Person:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = datetime.strptime(birthday, "%d-%m-%Y").date()

    def tinh_tuoi(self):
        today = date.today()
        # sửa lại công thức tính tuổi cho đúng
        age = today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )
        return age

    def in_thong_tin(self):
        return {
            "Name": self.name,
            "Country": self.country,
            "Birthday": self.birthday.strftime("%d-%m-%Y"),
            "Age": self.tinh_tuoi()
        }

class Person_Manager:
    def __init__(self, filename="BTVN01.json"):
        self.filename = filename
        self.people = self.doc_file()

    def tao_file(self):
        data = [
            {"name": "Tom", "country": "Viet Nam", "birthday": "12-07-1999"},
            {"name": "Alice", "country": "USA", "birthday": "01-01-1990"}     
        ]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.people =  [Person(p["name"], p["country"], p["birthday"]) for p in data]
        print("Ghi thành công")

    def doc_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                # sửa self.data → data
                self.people =  [Person(p["name"], p["country"], p["birthday"]) for p in data]
            print("Đọc file thành công")
            return self.people
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def luu_file(self):
        data = [p.in_thong_tin() for p in self.people]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def show_people(self):
        if not self.people:
            print("Danh sách rỗng")
            return 
        print("Danh sách người:")
        for i, p in enumerate(self.people, 1):
            info = p.in_thong_tin()
            print(f"{i}. {info['Name']} - {info['Country']} - {info['Birthday']} - Tuổi: {info['Age']}")

    def them_nguoi(self):
        print("Thêm người")
        name = input("Nhập tên người: ")
        country = input("Nhập quốc gia: ")
        birthday = input("Nhập ngày sinh (dd-mm-YYYY): ")
        try:
            datetime.strptime(birthday, "%d-%m-%Y")  # kiểm tra định dạng
        except ValueError:
            print("Ngày sinh không hợp lệ! Định dạng đúng là dd-mm-YYYY.")
            return
        self.people.append(Person(name, country, birthday))
        self.luu_file()
        print("Thêm thành công")

    def xoa_nguoi(self):
        try:
            index = int(input("Nhập vào số thứ tự người cần xóa: ")) - 1
        except ValueError:
            print("Phải nhập số!")
            return
        if index < 0 or index >= len(self.people):
            print("Không tồn tại trong danh sách")
            return
        del self.people[index]
        self.luu_file()
        print("Xóa người thành công")

    def xuat_tuoi(self):
        try:
            tuoi = int(input("Nhập vào tuổi cần tìm: "))
        except ValueError:
            print("Tuổi phải là số nguyên")
            return
        found = False
        for p in self.people:
            if p.tinh_tuoi() == tuoi:
                info = p.in_thong_tin()
                print(f"{info['Name']} - {info['Country']} - {info['Birthday']} - Tuổi: {info['Age']}")
                found = True
        if not found:
            print("Không tìm thấy người có tuổi này")
def menu():
    print("""
========= MENU =========
1. Tạo file mẫu
2. Hiển thị danh sách
3. Thêm người
4. Xóa người
5. Tìm theo tuổi
6. Thoát
========================
""")
    
def main():
    ds = Person_Manager()
    while True:
        menu()
        chon = input("Chọn chức năng: ")

        if chon == "1":
            ds.tao_file()
        elif chon == "2":
            ds.show_people()
        elif chon == "3":
            ds.them_nguoi()
        elif chon == "4":
            ds.xoa_nguoi()
        elif chon == "5":
            ds.xuat_tuoi()
        elif chon == "6":
            ds.luu_file()
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
if __name__ == "__main__":
    main()