from abc import ABC, abstractmethod
import math
class TinhToan(ABC):
    @abstractmethod
    def ChuVi(self):
        pass
    def DienTich(self):
        pass
class HinhTron(TinhToan):
    def __init__(self, r):
        self.r = r
    def ChuVi(self):
        return 2 * 3.14 * self.r
    def DienTich(self):
        return 3.14 * self.r * self.r
class HinhChuNhat(TinhToan):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def ChuVi(self):
        return (self.dai + self.rong) * 2
    def DienTich(self):
        return self.dai * self.rong
class HinhTamGiac(TinhToan):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def ChuVi(self):
        return self.a + self.b + self.c
    def DienTich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
r = float(input("Nhap ban kinh hinh tron: "))
hinhtron = HinhTron(r)
print(f"Chu vi hinh tron: {hinhtron.ChuVi()}")
print(f"Dien tich hinh tron: {hinhtron.DienTich():.2f}")
dai = int(input("Nhap chieu dai hinh chu nhat: "))
rong = int(input("Nhap chieu rong hinh chu nhat: "))
hinhchunhat = HinhChuNhat(dai, rong)
print(f"Chu vi hinh chu nhat: {hinhchunhat.ChuVi()}")
print(f"Dien tich hinh chu nhat: {hinhchunhat.DienTich()}")
a = int(input("Nhap canh a hinh tam giac: "))
b = int(input("Nhap canh b hinh tam giac: "))
c = int(input("Nhap canh c hinh tam giac: "))
hinhtamgiac = HinhTamGiac(a, b, c)
print(f"Chu vi hinh tam giac: {hinhtamgiac.ChuVi()}")
print(f"Dien tich hinh tam giac: {hinhtamgiac.DienTich():.2f}")
