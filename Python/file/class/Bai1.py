
class Person:
    def get_nguoi(self):
        print(f"Nguoi: {self.nguoi}")
    def get_nhanvien(self):
        print(f"Nhan vien: {self.nhanvien}")
    def get_sinhvien(self):
        print(f"Sinh vien: {self.sinhvien}")

class PersonInfo(Person):
    nguoi = "Nguyen Nhat Minh Quan"
    nhanvien = "Nguy Hao Nhien"
    sinhvien = "Luong Van Quan"

p1 = PersonInfo()
p1.get_nguoi()
p1.get_nhanvien()
p1.get_sinhvien()