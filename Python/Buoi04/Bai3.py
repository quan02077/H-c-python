class SanPham:
    def __init__(self,tenSp, giaSp, soLuongTrongKho):
        self.tenSp = tenSp
        self.giaSp = giaSp
        self.soLuongTrongKho = soLuongTrongKho
    def get_tenSp(self):
        return self.tenSp
    def get_giaSp(self):
        return self.giaSp
    def get_soLuongTrongKho(self):
        return self.soLuongTrongKho
class get_Price(SanPham):
    def gia(self, soLuongMua):
        if soLuongMua < 10:
            return self.giaSp * soLuongMua
        elif soLuongMua < 100:
            return self.giaSp * soLuongMua * 0.09
        else:
            return self.giaSp * soLuongMua * 0.08
class make_Purchase(get_Price):
    def mua(self, soLuongMua):
        if soLuongMua > self.soLuongTrongKho:
            print("Khong du so luong trong kho de mua")
        else:
            tongTien = self.gia(soLuongMua)
            print(f"Tong tien phai tra: {tongTien}")
            self.soLuongTrongKho -= soLuongMua
            print(f"So luong con lai trong kho: {self.soLuongTrongKho}")
tenSp = input("Nhap ten san pham: ")
giaSp = float(input("Nhap gia san pham: "))
soLuongTrongKho = int(input("Nhap so luong trong kho: "))
soLuongMua = int(input("Nhap so luong muon mua: "))
sp = make_Purchase(tenSp, giaSp, soLuongTrongKho)
sp.mua(soLuongMua)
print(f"Tong tien phai tra: {sp.gia(soLuongMua)}")
print(f"So luong con lai trong kho: {sp.get_soLuongTrongKho()}")
